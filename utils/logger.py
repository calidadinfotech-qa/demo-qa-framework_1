"""
Logging utility for the test automation framework
"""
import logging
import os
from datetime import datetime
from config.config import Config


class Logger:
    """Custom logger class for framework logging"""
    
    @staticmethod
    def get_logger(name=__name__):
        """
        Create and configure a logger instance
        
        Args:
            name (str): Logger name
            
        Returns:
            logging.Logger: Configured logger instance
        """
        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, Config.LOG_LEVEL))
        
        # Avoid duplicate handlers
        if logger.handlers:
            return logger
        
        # Create logs directory if it doesn't exist
        os.makedirs(Config.LOG_PATH, exist_ok=True)
        
        # Create file handler
        log_file = os.path.join(
            Config.LOG_PATH,
            f"test_execution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Add formatter to handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
