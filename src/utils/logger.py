import os
import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

rotate = TimedRotatingFileHandler(
    os.environ["LOGGING_FILEPATH"],
    when="D", # daily interval
    interval=1,
    backupCount=0,
    encoding=None,
    delay=False,
    utc=False,
) 

logger.addHandler(rotate)
formater = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
rotate.setFormatter(formater)
