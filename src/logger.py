import os
import pathlib

import logging
import logging.config

# load config
logging.config.fileConfig("configs/logging.ini", disable_existing_loggers=False)


def getLogger(name):
    return logging.getLogger(name)
