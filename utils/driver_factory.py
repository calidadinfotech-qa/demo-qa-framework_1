"""
Login Page Tests - Book Store Application
"""
from selenium import webdriver  # Import the selenium webdriver module
from selenium.webdriver.chrome.service import Service as ChromeService  # Import Chrome service to manage ChromeDriver
from selenium.webdriver.firefox.service import Service as FirefoxService  # Import Firefox service
from selenium.webdriver.edge.service import Service as EdgeService  # Import Edge service
from webdriver_manager.chrome import ChromeDriverManager  # Import ChromeDriverManager to automatically handle driver installation
from webdriver_manager.firefox import GeckoDriverManager  # Import GeckoDriverManager for Firefox
from webdriver_manager.microsoft import EdgeChromiumDriverManager  # Import EdgeChromiumDriverManager for Edge
from config.config import Config  # Import the Config class to access configuration settings


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
        # Determine which browser to use. Use the passed argument or fall back to the config default.
        browser = browser or Config.BROWSER
        # Normalize the browser string to lowercase to ensure case-insensitive comparison
        browser = browser.lower()
        
        if browser == "chrome":
            # Initialize ChromeOptions to configure Chrome-specific settings
            options = webdriver.ChromeOptions()
            # If HEADLESS mode is enabled in config, add the argument to run in background
            if Config.HEADLESS:
                options.add_argument("--headless")
            # Create a new Chrome instance with the specified service and options
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
            # Initialize FirefoxOptions for Firefox-specific settings
            options = webdriver.FirefoxOptions()
            # Check config to see if we should run headless
            if Config.HEADLESS:
                options.add_argument("--headless")
            
            # Initialize the Firefox driver using the installed GeckoDriver
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
            
        elif browser == "edge":
            # Initialize EdgeOptions
            options = webdriver.EdgeOptions()
            # Check for headless mode
            if Config.HEADLESS:
                options.add_argument("--headless")
            
            # Initialize the Edge driver
            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=options
            )
            
        else:
            # Raise an error if an unsupported browser is requested
            raise ValueError(f"Unsupported browser: {browser}")
        
        # Configure the driver with implicit wait time from config
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        # Set the page load timeout from config
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        
        # Set the window size based on configuration
        if Config.WINDOW_SIZE == "maximize":
            # Maximize the browser window
            driver.maximize_window()
        elif isinstance(Config.WINDOW_SIZE, tuple):
            # Set specific window dimensions if a tuple is provided
            driver.set_window_size(*Config.WINDOW_SIZE)
        
        # Return the configured driver instance
        return driver
