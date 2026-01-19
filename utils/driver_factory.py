"""
WebDriver Factory - Manages WebDriver initialization and configuration
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config.config import Config


class DriverFactory:
    """Factory class to create and configure WebDriver instances"""
    
    @staticmethod
    def get_driver(browser=None):
        """
        Create and return a WebDriver instance based on browser type
        
        Args:
            browser (str): Browser name (chrome, firefox, edge)
            
        Returns:
            WebDriver: Configured WebDriver instance
        """
        browser = browser or Config.BROWSER
        browser = browser.lower()
        
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if Config.HEADLESS:
                options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            
            # Get the driver path and ensure it's the actual executable
            driver_path = ChromeDriverManager().install()
            
            # Fix for macOS ARM64 - ensure we're using the actual chromedriver executable
            import os
            import stat
            if os.path.isdir(driver_path):
                # If it's a directory, find the chromedriver executable inside
                driver_path = os.path.join(driver_path, "chromedriver")
            elif "THIRD_PARTY_NOTICES" in driver_path or not driver_path.endswith("chromedriver"):
                # If it's pointing to the wrong file, get the directory and find chromedriver
                driver_dir = os.path.dirname(driver_path)
                driver_path = os.path.join(driver_dir, "chromedriver")
            
            # Ensure the chromedriver has execute permissions
            if os.path.exists(driver_path):
                os.chmod(driver_path, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
            
            driver = webdriver.Chrome(
                service=ChromeService(driver_path),
                options=options
            )
            
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if Config.HEADLESS:
                options.add_argument("--headless")
            
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
            
        elif browser == "edge":
            options = webdriver.EdgeOptions()
            if Config.HEADLESS:
                options.add_argument("--headless")
            
            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=options
            )
            
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
        # Configure driver
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        
        if Config.WINDOW_SIZE == "maximize":
            driver.maximize_window()
        elif isinstance(Config.WINDOW_SIZE, tuple):
            driver.set_window_size(*Config.WINDOW_SIZE)
        
        return driver
