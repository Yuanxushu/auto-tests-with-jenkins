import logging
import sys
from os.path import dirname, basename

# formatter = logging.Formatter("%(asctime)s - %(message)s")
# console = logging.StreamHandler(sys.stdout)
# console.setFormatter(formatter)

# BASE_NAME = basename(dirname(__file__))
# logging.basicConfig(filename="%s.log" % BASE_NAME, level=logging.INFO, format="%(asctime)s - %(message)s")
# logger = logging.getLogger(BASE_NAME)

# FAIL_LOGS = "failed_logs.log"
# err_logger = logging.getLogger(FAIL_LOGS)
# fileHandler = logging.FileHandler(FAIL_LOGS)
# fileHandler.setFormatter(formatter)
# err_logger.addHandler(fileHandler)

BASE_NAME = basename(dirname(__file__))
FAIL_LOGS = "failed_logs"


def create_logger(logger_name, level=logging.INFO):
    log_file = "%s.log" % logger_name
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    fileHandler = logging.FileHandler(log_file)
    fileHandler.setFormatter(formatter)

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)

    logger.setLevel(level)
    logger.addHandler(fileHandler)
    if level > logging.INFO:
        logger.addHandler(console)
    return logger


logger = create_logger(BASE_NAME)
err_logger = create_logger(FAIL_LOGS, level=logging.ERROR)

