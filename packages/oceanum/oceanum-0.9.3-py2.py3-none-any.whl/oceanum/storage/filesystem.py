import asyncio
import io
import os
import logging
import re
import weakref
from copy import copy
from urllib.parse import urlparse

import aiohttp
import fsspec
import requests
import yarl
import fsspec
from fsspec.asyn import AbstractAsyncStreamedFile, AsyncFileSystem, sync, sync_wrapper
from fsspec.callbacks import _DEFAULT_CALLBACK
from fsspec.exceptions import FSTimeoutError
from fsspec.spec import AbstractBufferedFile
from fsspec.utils import DEFAULT_BLOCK_SIZE, isfilelike, nullcontext, tokenize
from fsspec.implementations.memory import MemoryFile

DEFAULT_CONFIG = {"STORAGE_SERVICE": "https://storage.oceanum.io"}
fsspec.asyn._DEFAULT_BATCH_SIZE = 32

logger = logging.getLogger("fsspec.oceanum")


async def get_client(**kwargs):
    return aiohttp.ClientSession(**kwargs)


class FileSystem(AsyncFileSystem):
    """Datamesh storage filesystem.

    This follows the fsspec specification and can be used with dask.

    You can use this class directly, for example:
        fs = FileSystem(token="my_datamesh_token")
        fs.ls("/myfolder")

    or use fsspec convenience functions with protocol "oceanum". For example:
        of=fsspec.open("oceanum://myfolder/myfile.txt", token="my_datamesh_token")
    """

    def __init__(
        self,
        token=None,
        service=os.environ.get("STORAGE_SERVICE", DEFAULT_CONFIG["STORAGE_SERVICE"]),
        asynchronous=False,
        loop=None,
    ):
        """Storage filesystem constructor

        Args:
            token (string): Your datamesh access token. Defaults to os.environ.get("DATAMESH_TOKEN", None).
            service (string, optional): URL of datamesh service. Defaults to os.environ.get("STORAGE_SERVICE", "https://storage.oceanum.io").

        Raises:
            ValueError: Missing or invalid arguments
        """
        if token is None:
            token = os.environ.get("DATAMESH_TOKEN", None)
            if token is None:
                raise ValueError(
                    "A valid key must be supplied as a connection constructor argument or defined in environment variables as DATAMESH_TOKEN"
                )
        self._token = token
        url = urlparse(service)
        self._proto = url.scheme
        self._host = url.netloc
        self._base_url = f"{self._proto}://{self._host}/"
        self._auth_headers = {
            "X-DATAMESH-TOKEN": self._token,
        }
        super().__init__(self, asynchronous=asynchronous, loop=loop)
        self.get_client = get_client
        self.client_kwargs = {
            "headers": self._auth_headers,
            "timeout": aiohttp.ClientTimeout(total=60 * 60),
        }
        self._session = None

    @property
    def fsid(self):
        return "oceanum"

    @staticmethod
    def close_session(loop, session):
        if loop is not None and loop.is_running():
            try:
                sync(loop, session.close, timeout=0.1)
                return
            except (TimeoutError, FSTimeoutError):
                pass
        connector = getattr(session, "_connector", None)
        if connector is not None:
            # close after loop is dead
            connector._close()

    async def set_session(self):
        if self._session is None:
            self._session = await self.get_client(loop=self.loop, **self.client_kwargs)
            if not self.asynchronous:
                weakref.finalize(self, self.close_session, self.loop, self._session)
        return self._session

    async def _ls(self, path="", detail=True, **kwargs):
        logger.debug(path)
        session = await self.set_session()
        spath = path.strip("/")
        if len(spath) > 0:
            spath += "/"
        async with session.get(self._base_url + spath) as r:
            self._raise_not_found_for_status(r, path)
            listing = await r.json()
        if detail:
            return [
                {
                    **u,
                    "type": "directory" if u.get("contentType") == "folder" else "file",
                }
                for u in listing
            ]
        else:
            return [u["name"] for u in listing]

    ls = sync_wrapper(_ls)

    def _raise_not_found_for_status(self, response, url):
        """
        Raises FileNotFoundError for 404s, otherwise uses raise_for_status.
        """
        if response.status == 404:
            raise FileNotFoundError(url)
        response.raise_for_status()

    async def _cat_file(self, path, **kwargs):
        logger.debug(path)
        session = await self.set_session()
        async with session.get(self._base_url + path.strip("/")) as r:
            out = await r.read()
            self._raise_not_found_for_status(r, path)
        return out

    async def _get_file(
        self, rpath, lpath, chunk_size=5 * 2**20, callback=_DEFAULT_CALLBACK, **kwargs
    ):
        logger.debug(rpath)
        if rpath[-1] == "/":
            os.makedirs(lpath, exist_ok=True)
            return
        session = await self.set_session()
        async with session.get(self._base_url + rpath.lstrip("/")) as r:
            try:
                size = int(r.headers["content-length"])
            except (ValueError, KeyError):
                size = None

            callback.set_size(size)
            self._raise_not_found_for_status(r, rpath)
            if isfilelike(lpath):
                outfile = lpath
            else:
                outfile = open(lpath, "wb")

            try:
                chunk = True
                while chunk:
                    chunk = await r.content.read(chunk_size)
                    outfile.write(chunk)
                    callback.relative_update(len(chunk))
            finally:
                if not isfilelike(lpath):
                    outfile.close()

    async def _put_file(
        self,
        lpath,
        rpath,
        chunk_size=5 * 2**20,
        callback=_DEFAULT_CALLBACK,
        method="post",
        **kwargs,
    ):
        async def gen_chunks():
            # Support passing arbitrary file-like objects
            # and use them instead of streams.
            if isinstance(lpath, io.IOBase):
                context = nullcontext(lpath)
                use_seek = False  # might not support seeking
            else:
                context = open(lpath, "rb")
                use_seek = True

            with context as f:
                if use_seek:
                    callback.set_size(f.seek(0, 2))
                    f.seek(0)
                else:
                    callback.set_size(getattr(f, "size", None))

                chunk = f.read(chunk_size)
                while chunk:
                    yield chunk
                    callback.relative_update(len(chunk))
                    chunk = f.read(chunk_size)

        session = await self.set_session()

        method = method.lower()
        if method not in ("post", "put"):
            raise ValueError(
                f"method has to be either 'post' or 'put', not: {method!r}"
            )

        meth = getattr(session, method)
        async with meth(self._base_url + rpath.strip("/"), data=gen_chunks()) as resp:
            self._raise_not_found_for_status(resp, rpath)

    async def _exists(self, path, **kwargs):
        try:
            logger.debug(path)
            session = await self.set_session()
            r = await session.get(self._base_url + path.lstrip("/"))
            async with r:
                return r.status < 400
        except (requests.HTTPError, aiohttp.ClientError):
            return False

    async def _isfile(self, path):
        try:
            info = await self._info(path)
            return info["type"] == "file"
        except:
            return False

    async def _isdir(self, path):
        try:
            info = await self._info(path)
            return info["type"] == "directory"
        except OSError:
            return False

    async def _open(
        self,
        path,
        mode="rb",
        chunk_size=5 * 2**8,
        **kwargs,
    ):
        if mode != "rb":
            raise NotImplementedError
        logger.debug(path)
        session = await self.set_session()
        async with session.get(self._base_url + path.strip("/")) as r:
            try:
                size = int(r.headers["content-length"])
            except (ValueError, KeyError):
                size = None

            self._raise_not_found_for_status(r, path)
            f = MemoryFile(None, None)
            try:
                chunk = True
                while chunk:
                    chunk = await r.content.read(chunk_size)
                    f.write(chunk)
            finally:
                f.seek(0)
            return f

    async def _info(self, path, **kwargs):
        """Get info of path"""
        info = {}
        session = await self.set_session()
        async with session.head(self._base_url + path.lstrip("/")) as r:
            self._raise_not_found_for_status(r, path)
        return {
            "name": path,
            "size": int(r.headers.get("content-length")),
            "contentType": r.headers.get("content-type"),
            "modified": r.headers.get("last-modified"),
            "type": "directory"
            if r.headers.get("content-type") == "folder"
            else "file",
        }

    async def _mkdir(self, path, create_parents=True, **kwargs):
        logger.debug(path)
        if create_parents:
            await self._makedirs(path, exist_ok=True)
        else:
            await self._makedirs(path, exist_ok=False)

    async def _makedirs(self, path, exist_ok=False):
        logger.debug(path)
        if not exist_ok:
            check = await self._exists(path)
            if check:
                raise FileExistsError(path)
        session = await self.set_session()
        async with session.put(self._base_url + path.strip("/") + "/_") as r:
            self._raise_not_found_for_status(r, path)

    def ukey(self, path):
        """Unique identifier"""
        return tokenize(path)
