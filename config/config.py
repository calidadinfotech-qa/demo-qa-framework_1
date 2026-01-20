"""
Configuration management for the test automation framework.
Contains all configuration settings, URLs, timeouts, and test data.
"""


class Config:
    """Main configuration class for the framework"""
    
    # Base URL of the application under test (DemoQA)
    BASE_URL = "https://demoqa.com"
    
    # Browser settings - determines which browser the tests will run on
    BROWSER = "chrome"  # Options: chrome, firefox, edge
    HEADLESS = False    # Set to True to run tests without a visible UI
    
    # Timeouts (in seconds) to handle synchronization issues
    IMPLICIT_WAIT = 10         # Default wait time for finding elements
    EXPLICIT_WAIT = 15         # Maximum time to wait for specific conditions
    PAGE_LOAD_TIMEOUT = 30     # Maximum time to wait for a page to load
    
    # Window settings
    WINDOW_SIZE = "maximize"  # or tuple like (1920, 1080) for custom resolution
    
    # Screenshot settings for debugging failures
    SCREENSHOT_ON_FAILURE = True   # Automatically capture screenshot on test failure
    SCREENSHOT_PATH = "screenshots"  # Directory to save screenshots
    
    # Logging settings
    LOG_LEVEL = "INFO"  # Logging level (INFO, DEBUG, ERROR)
    LOG_PATH = "logs"   # Directory to save log files
    
    # Report settings
    REPORT_PATH = "reports"  # Directory to save HTML/Allure reports
    
    # Test data - Default credentials
    VALID_USERNAME = "testuser"
    VALID_PASSWORD = "Test@123"
    
    # Page URLs - constructed dynamically using the BASE_URL
    LOGIN_URL = f"{BASE_URL}/login"
    TEXT_BOX_URL = f"{BASE_URL}/text-box"
    BUTTONS_URL = f"{BASE_URL}/buttons"
    WEB_TABLES_URL = f"{BASE_URL}/webtables"
    FORMS_URL = f"{BASE_URL}/automation-practice-form"
