import os
import pathlib

import logging
import logging.config

_config_file_name = "logging.ini"

_config_file_path = os.path.join(
    pathlib.Path(__file__).parent.resolve(), _config_file_name
)

# load config
logging.config.fileConfig(_config_file_path, disable_existing_loggers=False)

logger = logging.getLogger(__name__)
