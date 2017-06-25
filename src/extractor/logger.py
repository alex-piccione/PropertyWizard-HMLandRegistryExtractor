import os
import logging

log_level = logging.INFO

class Logger:

    @staticmethod
    def create(name, log_min_level=log_level, folder="logs") -> logging:

        log_file = os.path.join(os.getcwd(), "{0}\{1}.log".format(folder, name))
        log_dir = os.path.dirname(log_file)
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        logger = logging.getLogger(name)
        logger.setLevel(log_min_level)
        handler = logging.FileHandler(log_file)
        handler.setLevel(log_min_level)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger


