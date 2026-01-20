"""
Base Page class - Contains common methods for all page objects
"""
import os  # Operations with the operating system
import time  # Time operations for delays
from datetime import datetime  # Date and time operations
from selenium.webdriver.support.ui import WebDriverWait  # Explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Expected conditions for waits
from selenium.common.exceptions import TimeoutException, NoSuchElementException  # Exception handling
from config.config import Config  # Import configuration constants
from utils.logger import Logger  # Import Logger class


class BasePage:
    """Base class for all page objects, providing wrapper methods for Selenium actions"""
    
    def __init__(self, driver):
        """
        Initialize BasePage with the WebDriver instance
        
        Args:
            driver: WebDriver instance passed from the test
        """
        self.driver = driver
        # Initialize an explicit wait with the configured timeout
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        # Initialize logger for this class
        self.logger = Logger.get_logger(self.__class__.__name__)
    
    def find_element(self, locator):
        """
        Find a single element with explicit wait.
        Waits until the element is present in the DOM.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
            
        Returns:
            WebElement: Found element
        """
        try:
            # Wait until element is located
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.debug(f"Element found: {locator}")
            return element
        except TimeoutException:
            # Log error if timeout occurs
            self.logger.error(f"Element not found: {locator}")
            raise
    
    def find_elements(self, locator):
        """
        Find multiple elements with explicit wait.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
            
        Returns:
            list: List of WebElements. Returns empty list if none found.
        """
        try:
            # Wait until all elements are present
            elements = self.wait.until(EC.presence_of_all_elements_located(locator))
            self.logger.debug(f"Elements found: {locator}, count: {len(elements)}")
            return elements
        except TimeoutException:
            self.logger.error(f"Elements not found: {locator}")
            return []
    
    def click(self, locator):
        """
        Click on an element.
        Waits until the element is clickable before clicking.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
        """
        # Wait until element is visible and enabled
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)  # Slow down for visual verification
        element.click()
        self.logger.info(f"Clicked on element: {locator}")
    
    def send_keys(self, locator, text, clear_first=True):
        """
        Type text into an input field.
        Optionally clears the field first.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
            text (str): Text to type
            clear_first (bool): Clear field before typing (default: True)
        """
        element = self.find_element(locator)
        if clear_first:
            element.clear()  # Clear existing text
        time.sleep(0.5)  # Small delay before typing
        element.send_keys(text)  # Send the new text
        self.logger.info(f"Typed '{text}' into element: {locator}")
        time.sleep(0.5)  # Small delay after typing
    
    def get_text(self, locator):
        """
        Get the visible text from an element.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
            
        Returns:
            str: Element text
        """
        element = self.find_element(locator)
        text = element.text
        self.logger.debug(f"Got text '{text}' from element: {locator}")
        return text
    
    def is_displayed(self, locator):
        """
        Check if an element is currently displayed (visible) on the page.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
            
        Returns:
            bool: True if displayed, False otherwise
        """
        try:
            element = self.find_element(locator)
            is_visible = element.is_displayed()
            self.logger.debug(f"Element {locator} displayed: {is_visible}")
            return is_visible
        except (TimeoutException, NoSuchElementException):
            return False
    
    def wait_for_element(self, locator, timeout=None):
        """
        Specific wait for an element to be present, allowing custom timeout.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
            timeout (int): Custom timeout in seconds (optional)
            
        Returns:
            WebElement: Found element
        """
        timeout = timeout or Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def take_screenshot(self, name="screenshot"):
        """
        Capture a screenshot and save it to the screenshots directory.
        
        Args:
            name (str): Prefix name for the screenshot file
            
        Returns:
            str: Absolute file path of the saved screenshot
        """
        # Create directory if it doesn't exist
        os.makedirs(Config.SCREENSHOT_PATH, exist_ok=True)
        # Generate timestamp for unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(Config.SCREENSHOT_PATH, filename)
        # Save the screenshot
        self.driver.save_screenshot(filepath)
        self.logger.info(f"Screenshot saved: {filepath}")
        return filepath
    
    def scroll_to_element(self, locator):
        """
        Scroll the page view until the element is visible.
        Uses JavaScript execution.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
        """
        element = self.find_element(locator)
        # Execute JS to scroll
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.logger.debug(f"Scrolled to element: {locator}")
    
    def get_current_url(self):
        """
        Get the current active page URL.
        
        Returns:
            str: Current URL
        """
        return self.driver.current_url
    
    def get_title(self):
        """
        Get the current page title.
        
        Returns:
            str: Page title
        """
        return self.driver.title
