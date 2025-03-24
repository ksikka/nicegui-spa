import os
from dataclasses import dataclass
from pathlib import Path
import time
import config
from nicegui import run


@dataclass
class Model:
    name: str
    creation_timestamp: float
    creation_timestamp_fmt: str

    @classmethod
    def list(cls):
        file_info = []
        with os.scandir(config.model_dir) as entries:
            for entry in entries:
                if not entry.is_dir():
                    continue
                try:
                    creation_timestamp = entry.stat().st_birthtime
                except AttributeError:
                    creation_timestamp = entry.stat().st_ctime
                creation_timestamp_fmt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(creation_timestamp))
                file_info.append(cls(entry.name, creation_timestamp, creation_timestamp_fmt))

        return file_info

    @classmethod
    async def async_list(cls):
        return await run.io_bound(cls.list)
