import sys
import logging
import os
import atexit  # Import the atexit module
import inspect
from logging.handlers import TimedRotatingFileHandler

# Log levels
LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARN": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

LOGGER_NAME=__name__
LOG_DIR="log"
LOGFILE_NAME="project.log"
LOG_BACKUP_COUNT = 30
LOG_DURATION = "midnight"

class Logger(object):
    loggers = {}  # Class variable to store logger instances
    
    @classmethod
    def FUNC_NAME(self):
        return inspect.stack()[1][3]

    @classmethod
    def set_stream_handler(cls, logger):
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(LOG_LEVELS['INFO'])
        log_format = "%(asctime)s - %(levelname)s - %(module)s - line : %(lineno)d - %(message)s \n"
        stream_handler.setFormatter(logging.Formatter(log_format, datefmt="%d-%m-%Y %H:%M:%S"))
        logger.addHandler(stream_handler)
        print("STREAM LOGGER ADDED")
        return logger

    @staticmethod
    def set_handler(logger_name=LOGGER_NAME, log_dir=LOG_DIR, log_filename=LOGFILE_NAME, log_backup_count=LOG_BACKUP_COUNT, log_duration=LOG_DURATION, log_level=LOG_LEVELS["INFO"]):
        if logger_name in Logger.loggers:
            return Logger.loggers[logger_name]  # Return the existing logger if it exists

        logger = logging.getLogger(logger_name)
        log_filename = log_filename
        logger = Logger.set_stream_handler(logger)
        logger.addHandler(
            Logger.get_handler(
                log_dir=log_dir,
                log_filename=log_filename,
                log_level=log_level,
                log_backup_count=log_backup_count,
                log_duration=log_duration
            )
        )
        Logger.loggers[logger_name] = logger  # Store the logger instance
        return logger

    @staticmethod
    def get_handler(log_dir="log/", log_filename="dg_batch_loader.log", log_level=None, log_backup_count=1, log_duration='daily'):
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, True)
            os.chmod(log_dir, mode=0o777)
            with open(os.path.join(log_dir, ".gitkeep"), "w") as fp:
                pass

        logging_level = LOG_LEVELS["INFO"]
        logging.basicConfig(level=logging_level)
        file_path = os.path.join(log_dir, log_filename)
        handler = TimedRotatingFileHandler(
            file_path, when=log_duration, interval=1, delay=True, backupCount=log_backup_count
        )
        log_format = "%(asctime)s - %(levelname)s - %(module)s - line : %(lineno)d - %(message)s \n"
        handler.setFormatter(logging.Formatter(log_format, datefmt="%d-%m-%Y %H:%M:%S"))

        return handler

    @staticmethod
    def closeLogger(logger):
        # Iterate over the logger's handlers and remove them
        for handler in logger.handlers[:]:  # Use a copy of the list
            if isinstance(handler, TimedRotatingFileHandler):
                handler.close()
            logger.removeHandler(handler)

# atexit.register(Logger.closeLogger)  # Register the closeLogger method to be called at program exit

