import logging

# This creates a logger with the name of the module "logging_helper"
logger = logging.getLogger(__name__)
logger.info("hello from helper")


# log handler objects dispatch appropiate log messages to to the handlers 
# specific destination.

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("logging_file.log")

# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("this is a warning")
logger.error("this an error")
