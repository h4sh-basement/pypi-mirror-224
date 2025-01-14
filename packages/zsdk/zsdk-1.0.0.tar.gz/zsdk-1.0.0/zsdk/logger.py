import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(
    name: str,
    level: str = os.getenv("LOGGING_LEVEL", "info"),
    log_filename: str = "output.log",
    max_log_size: int = 10 * 1024 * 1024,  # 10 MB
    backup_count: int = 3,
) -> logging.Logger:
    """
    To set up as many loggers as you want

    Args:
        name (str): Name of logger
        level (str): os.getenv("LOGGING_LEVEL"). Defaults to 'info'.
        log_filename (str): Name and Path of log file.  Defaults to "output.log"
        max_log_size (int): Defaults to 10MB
        backup_count (int): Default to 3

    Return:
        Logger Object
    """
    handler_stream = logging.StreamHandler()
    handler_file = RotatingFileHandler(
        log_filename,
        maxBytes=max_log_size,
        backupCount=backup_count,
    )
    formatter = logging.Formatter(
        fmt="{asctime} {name}.{funcName} {levelname} {message}",
        datefmt="%Y%m%d %H:%M:%S",
        style="{",
    )
    handler_stream.setFormatter(formatter)
    handler_file.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.addHandler(handler_stream)
    logger.addHandler(handler_file)

    log_level = logging.INFO
    level = level.lower()
    if level == "notset":
        log_level = logging.NOTSET
    elif level == "debug":
        log_level = logging.DEBUG
    elif level == "info":
        log_level = logging.INFO
    elif level == "warning" or level == "warn":
        log_level = logging.WARNING
    elif level == "error":
        log_level = logging.ERROR
    elif level == "critical":
        log_level = logging.CRITICAL
    logger.setLevel(log_level)

    return logger
