"""
Pytest configuration file - Contains fixtures and hooks that allow tests to share setup/teardown logic.
"""
import pytest
import os
from datetime import datetime
from utils.driver_factory import DriverFactory
from config.config import Config


@pytest.fixture(scope="function")
def driver():
    """
    WebDriver fixture - Creates and quits driver for each test function.
    'scope="function"' means this fixture is re-run for every test.
    
    Yields:
        WebDriver: Browser driver instance ready for use
    """
    # Create driver instance using logic in DriverFactory
    driver = DriverFactory.get_driver()
    # 'yield' acts like return, but allows code execution after the test finishes (teardown)
    yield driver
    # Cleanup: Close the browser window
    driver.quit()


@pytest.fixture(scope="function")
def setup_teardown(driver):
    """
    Setup and teardown fixture for additional test preparation.
    Depends on the 'driver' fixture.
    
    Args:
        driver: WebDriver instance from the driver fixture
        
    Yields:
        WebDriver: Browser driver instance
    """
    # Setup step: Maximize window to ensure all elements are visible
    driver.maximize_window()
    
    # Pass control to the test function
    yield driver
    
    # Teardown step: Clear cookies to ensure clean state for next test
    driver.delete_all_cookies()


def pytest_runtest_makereport(item, call):
    """
    Pytest hook to capture screenshot on test failure.
    Executed after each test phase (setup, call, teardown).
    
    Args:
        item: Test item (the test function)
        call: Test call info (result, exception info, etc.)
    """
    # Check if the phase is "call" (actual test execution)
    if call.when == "call":
        # Check if an exception occurred (test failed)
        if call.excinfo is not None:
            # Retrieve the driver from the test's fixtures
            driver = item.funcargs.get('driver')
            if driver and Config.SCREENSHOT_ON_FAILURE:
                # Ensure screenshot directory exists
                os.makedirs(Config.SCREENSHOT_PATH, exist_ok=True)
                # Generate unique filename with timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_name = f"{item.name}_{timestamp}.png"
                screenshot_path = os.path.join(Config.SCREENSHOT_PATH, screenshot_name)
                # Save screenshot
                driver.save_screenshot(screenshot_path)
                print(f"\nScreenshot saved: {screenshot_path}")


@pytest.fixture(scope="session", autouse=True)
def create_directories():
    """
    Create necessary directories before test execution starts.
    'scope="session"' means run once per test session.
    'autouse=True' means run automatically without being requested.
    """
    os.makedirs(Config.SCREENSHOT_PATH, exist_ok=True)
    os.makedirs(Config.LOG_PATH, exist_ok=True)
    os.makedirs(Config.REPORT_PATH, exist_ok=True)
