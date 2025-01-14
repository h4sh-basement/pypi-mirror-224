import os

from typing import Optional

from polyaxon.connections import CONNECTION_CONFIG
from polyaxon.contexts import paths as ctx_paths
from polyaxon.env_vars.getters import get_artifacts_store_name
from polyaxon.env_vars.keys import EV_KEYS_SANDBOX_IS_LOCAL
from polyaxon.fs.fs import close_fs, get_async_fs_from_connection, get_default_fs
from polyaxon.fs.types import FSSystem


class AppFS:
    _connections = {}

    @classmethod
    async def set_fs(cls, connection: Optional[str] = None) -> FSSystem:
        fs = None
        if connection:
            name = connection
            connection = CONNECTION_CONFIG.get_connection_for(connection)
            if connection:
                fs = await get_async_fs_from_connection(connection=connection)
        else:
            fs = await get_default_fs()
            name = get_artifacts_store_name()

        cls._connections[name] = fs
        return cls._connections[name]

    @classmethod
    async def close_fs(cls, connection: Optional[str] = None):
        connection = connection or get_artifacts_store_name()
        fs = cls._connections.get(connection)
        await close_fs(fs)

    @classmethod
    async def get_fs(cls, connection: Optional[str] = None) -> FSSystem:
        if not connection or os.environ.get(EV_KEYS_SANDBOX_IS_LOCAL):
            connection = get_artifacts_store_name()
        fs = cls._connections.get(connection)
        if not fs:
            return await cls.set_fs(connection=connection)
        return fs

    @staticmethod
    def get_fs_root_path(connection: Optional[str] = None) -> str:
        connection = connection or get_artifacts_store_name()
        connection = CONNECTION_CONFIG.get_connection_for(connection)
        if not connection:
            return ctx_paths.CONTEXT_ARTIFACTS_ROOT
        return connection.store_path
