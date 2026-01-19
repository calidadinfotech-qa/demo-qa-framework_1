"""
Pytest configuration file - Contains fixtures and hooks
"""
import pytest
import os
from datetime import datetime
from utils.driver_factory import DriverFactory
from config.config import Config


@pytest.fixture(scope="function")
def driver():
    """
    WebDriver fixture - Creates and quits driver for each test
    
    Yields:
        WebDriver: Browser driver instance
    """
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def setup_teardown(driver):
    """
    Setup and teardown fixture
    
    Args:
        driver: WebDriver instance
        
    Yields:
        WebDriver: Browser driver instance
    """
    # Setup
    driver.maximize_window()
    
    yield driver
    
    # Teardown
    driver.delete_all_cookies()


def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on test failure
    
    Args:
        item: Test item
        call: Test call
    """
    if call.when == "call":
        if call.excinfo is not None:
            # Test failed
            driver = item.funcargs.get('driver')
            if driver and Config.SCREENSHOT_ON_FAILURE:
                os.makedirs(Config.SCREENSHOT_PATH, exist_ok=True)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_name = f"{item.name}_{timestamp}.png"
                screenshot_path = os.path.join(Config.SCREENSHOT_PATH, screenshot_name)
                driver.save_screenshot(screenshot_path)
                print(f"\nScreenshot saved: {screenshot_path}")


@pytest.fixture(scope="session", autouse=True)
def create_directories():
    """Create necessary directories before test execution"""
    os.makedirs(Config.SCREENSHOT_PATH, exist_ok=True)
    os.makedirs(Config.LOG_PATH, exist_ok=True)
    os.makedirs(Config.REPORT_PATH, exist_ok=True)
