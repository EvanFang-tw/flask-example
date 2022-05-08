import os
import pathlib

import logging
import logging.config

from utils import get_file_dir

_config_file_path = os.path.join(get_file_dir(__file__), "logging.ini")

# load config
logging.config.fileConfig(_config_file_path, disable_existing_loggers=False)


def getLogger(name):
    return logging.getLogger(name)
