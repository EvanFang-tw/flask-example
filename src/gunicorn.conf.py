import os

from logger import getLogger

logger = getLogger("gunicorn.conf")

GUNICORN_PORT = os.getenv("GUNICORN_PORT", "8888")
GUNICORN_WORKERS = os.getenv("GUNICORN_WORKERS", "1")
GUNICORN_RELOAD = os.getenv("GUNICORN_RELOAD", "False")

bind = f"0.0.0.0:8888"
workers = int(GUNICORN_WORKERS)
reload = GUNICORN_RELOAD.upper() in ["TRUE", "1", "OK"]

logger.info(f"bind: {bind}")
logger.info(f"workers: {workers}")
logger.info(f"reload: {reload}")
