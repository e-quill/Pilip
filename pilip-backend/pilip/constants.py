import os
from datetime import datetime

from pydantic import BaseModel


def _redis_configs(self):

    configs = {}

    configs["host"] = os.getenv("REDIS_HOST", "localhost")
    configs["port"] = os.getenv("REDIS_PORT", 6379)
    configs["username"] = os.getenv("REDIS_USER", "root")
    configs["password"] = os.getenv("REDIS_PASS", "root")

    return configs


class Config:

    DEBUG = os.getenv("DEBUG", "false") == "true"
    STARTUP = datetime.now()
    DB_URL = os.getenv("DB_URL")
    REDIS_URL = os.getenv("REDIS_URL", "redis://root:root@localhost:6379/")

    def since_startup():
        duration = datetime.now() - Config.STARTUP

        return f"{round(duration.seconds/60)} minutes."
