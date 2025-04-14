import logging

# We can log to 5 different severity levels
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

# By default only messages at warning level or above are printed
# To change this, we can set the base configuration, directly after importing
# the logging library
logging.basicConfig(
  level = logging.DEBUG
  , format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  , datefmt = "%m/%d/%Y %H:%M:%S"
)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# by defaut the logger is called root. 
# If we want to log different modules, it is best practice to no use the root 
# logger but to create our own in the corresponding module.
import logging_helper


# Capturing stack traces in the log.
# This can help troubleshooting
try:
  a = [1, 2, 3]
  val = a[4]
except IndexError as e:
  logging.error(e, exc_info = True)

import traceback

try:
  a = [1, 2, 3]
  val = a[4]
except:
  logging.error("The error is %s", traceback.format_exc())

# rotating file handlers
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("rotating_logger")
logger.setLevel(logging.INFO)

## Roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc.
handler = RotatingFileHandler("app.log", maxBytes = 2000, backupCount = 5)
logger.addHandler(handler)

for _ in range(10000):
  logger.info("Hello, world!")


## timed rotating handlers
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger("rotating_logger")
logger.setLevel(logging.INFO)

## Roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc.
handler = TimedRotatingFileHandler(
  "timed_test.log"
  # when to roll over: s (seconds), m (minutes), h (hours), d (days), midnight,
  # w0 (monday), w1 (tuesday), ...
  , when = "s"
  #  a new log file is created every 5 seconds
  , interval = 1
  , backupCount = 5
)
logger.addHandler(handler)

for _ in range(6):
  logger.info("Hello, world!")
  time.sleep(5)





