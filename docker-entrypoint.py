#!/usr/bin/env python

import os
from copy import deepcopy
from pathlib import Path

from redbot.core import data_manager, drivers
from redbot.core.drivers import BackendType
from redbot.setup import appdir, save_config

name = os.getenv("REDBOT_NAME", "redbot")
storage_type_value = os.getenv("REDBOT_STORAGE_TYPE", BackendType.JSON.value)
storage_type: BackendType = BackendType[storage_type_value]

data_path = Path(appdir.user_data_dir) / "data" / name

if not data_path.exists():
    data_path.mkdir(parents=True, exist_ok=True)

default_data_dir = str(data_path.resolve())
driver_cls = drivers.get_driver_class(storage_type)

default_dirs = deepcopy(data_manager.basic_config_default)
default_dirs["DATA_PATH"] = default_data_dir
default_dirs["STORAGE_TYPE"] = storage_type.value
default_dirs["STORAGE_DETAILS"] = {}

if storage_type == BackendType.POSTGRES \
        or storage_type == storage_type.MONGO \
        or storage_type == storage_type.MONGOV1:
    host = os.getenv("REDBOT_DB_HOST")
    port = os.getenv("REDBOT_DB_PORT")
    user = os.getenv("REDBOT_DB_USER")
    password = os.getenv("REDBOT_DB_PASS")
    database = os.getenv("REDBOT_DB_NAME")

    if storage_type == storage_type.POSTGRES:
        default_dirs["STORAGE_DETAILS"] = {
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "database": database,
        }

    if storage_type == storage_type.MONGO \
            or storage_type == storage_type.MONGOV1:
        default_dirs["STORAGE_DETAILS"] = {
            "HOST": host,
            "PORT": port,
            "USERNAME": user,
            "PASSWORD": password,
            "DB_NAME": database,
            "URI": "mongodb",
        }

save_config(name, default_dirs)
