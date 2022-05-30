import os
import logging
import logging.config

# load config
logging.config.fileConfig("configs/logging.ini", disable_existing_loggers=False)
# logging.basicConfig(
#     stream=sys.stdout,
#     format="%(asctime)s.%(msecs)03dZ [%(levelname)s] %(name)s: %(message)s",
#     datefmt="%Y-%m-%dT%H:%M:%S",
# )

def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, os.getenv("LOG_LEVEL", "INFO")))
    return logger
