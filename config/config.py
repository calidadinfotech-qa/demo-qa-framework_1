"""
Configuration management for the test automation framework.
Contains all configuration settings, URLs, timeouts, and test data.
"""

class Config:
    """Main configuration class for the framework"""
    
    # Base URL
    BASE_URL = "https://demoqa.com"
    
    # Browser settings
    BROWSER = "chrome"  # Options: chrome, firefox, edge
    HEADLESS = False
    
    # Timeouts (in seconds)
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15
    PAGE_LOAD_TIMEOUT = 30
    
    # Window settings
    WINDOW_SIZE = "maximize"  # or tuple like (1920, 1080)
    
    # Screenshot settings
    SCREENSHOT_ON_FAILURE = True
    SCREENSHOT_PATH = "screenshots"
    
    # Logging settings
    LOG_LEVEL = "INFO"
    LOG_PATH = "logs"
    
    # Report settings
    REPORT_PATH = "reports"
    
    # Test data
    VALID_USERNAME = "testuser"
    VALID_PASSWORD = "Test@123"
    
    # Page URLs
    LOGIN_URL = f"{BASE_URL}/login"
    TEXT_BOX_URL = f"{BASE_URL}/text-box"
    BUTTONS_URL = f"{BASE_URL}/buttons"
    WEB_TABLES_URL = f"{BASE_URL}/webtables"
    FORMS_URL = f"{BASE_URL}/automation-practice-form"
