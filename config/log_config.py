import logging
import os


class LoggerConfig:
    # Logging configuration
    LOGGING_LEVEL = logging.INFO
    LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

    def __init__(self, log_filename='test.log'):
        # Create logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.LOGGING_LEVEL)

        # Create a file handler and set the logging level
        log_file_path = os.path.join(os.getcwd(), 'log', log_filename)
        self.file_handler = logging.FileHandler(log_file_path)
        self.file_handler.setLevel(self.LOGGING_LEVEL)

        # Create a formatter and add it to the file handler
        formatter = logging.Formatter(self.LOGGING_FORMAT, datefmt='%Y-%m-%d %H:%M:%S')
        self.file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        self.logger.addHandler(self.file_handler)

    def close_logger(self):
        # Remove the file handler from the logger and close the file handler
        self.logger.removeHandler(self.file_handler)
        self.file_handler.close()


"""
Example usage:
config_instance = LoggerConfig()
config_instance.logger.info("This is a test log message.")
"""