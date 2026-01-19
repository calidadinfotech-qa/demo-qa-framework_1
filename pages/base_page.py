"""
Base Page class - Contains common methods for all page objects
"""
import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.config import Config
from utils.logger import Logger


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        """
        Initialize BasePage
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.logger = Logger.get_logger(self.__class__.__name__)
    
    def find_element(self, locator):
        """
        Find an element with explicit wait
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
            
        Returns:
            WebElement: Found element
        """
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.debug(f"Element found: {locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Element not found: {locator}")
            raise
    
    def find_elements(self, locator):
        """
        Find multiple elements
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
            
        Returns:
            list: List of WebElements
        """
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(locator))
            self.logger.debug(f"Elements found: {locator}, count: {len(elements)}")
            return elements
        except TimeoutException:
            self.logger.error(f"Elements not found: {locator}")
            return []
    
    def click(self, locator):
        """
        Click on an element
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        self.logger.info(f"Clicked on element: {locator}")
    
    def send_keys(self, locator, text, clear_first=True):
        """
        Type text into an element
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
            text (str): Text to type
            clear_first (bool): Clear field before typing
        """
        element = self.find_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)
        self.logger.info(f"Typed '{text}' into element: {locator}")
    
    def get_text(self, locator):
        """
        Get text from an element
        
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
        Check if element is displayed
        
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
        Wait for element to be present
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
            timeout (int): Custom timeout in seconds
            
        Returns:
            WebElement: Found element
        """
        timeout = timeout or Config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    def take_screenshot(self, name="screenshot"):
        """
        Take a screenshot
        
        Args:
            name (str): Screenshot name
            
        Returns:
            str: Screenshot file path
        """
        os.makedirs(Config.SCREENSHOT_PATH, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(Config.SCREENSHOT_PATH, filename)
        self.driver.save_screenshot(filepath)
        self.logger.info(f"Screenshot saved: {filepath}")
        return filepath
    
    def scroll_to_element(self, locator):
        """
        Scroll to an element
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "value")
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.logger.debug(f"Scrolled to element: {locator}")
    
    def get_current_url(self):
        """
        Get current page URL
        
        Returns:
            str: Current URL
        """
        return self.driver.current_url
    
    def get_title(self):
        """
        Get page title
        
        Returns:
            str: Page title
        """
        return self.driver.title
