import os
import logging
import logging.config

# load config
logging.config.fileConfig("configs/logging.ini", disable_existing_loggers=False)


def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, os.getenv("LOG_LEVEL", "INFO")))
    return logger
