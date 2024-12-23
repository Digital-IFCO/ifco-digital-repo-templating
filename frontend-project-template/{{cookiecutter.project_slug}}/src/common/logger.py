import logging
import sys


def setup_logger(log_level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    if not logger.handlers:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(stream_handler)
    return logger
