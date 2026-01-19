"""
Buttons Page Object - Elements > Buttons
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class ButtonsPage(BasePage):
    """Page Object for Buttons Page"""
    
    # Locators
    DOUBLE_CLICK_BUTTON = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.ID, "rightClickBtn")
    DYNAMIC_CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    DOUBLE_CLICK_MESSAGE = (By.ID, "doubleClickMessage")
    RIGHT_CLICK_MESSAGE = (By.ID, "rightClickMessage")
    DYNAMIC_CLICK_MESSAGE = (By.ID, "dynamicClickMessage")
    
    def __init__(self, driver):
        """Initialize ButtonsPage"""
        super().__init__(driver)
        self.actions = ActionChains(driver)
    
    def navigate_to_buttons(self):
        """Navigate to buttons page"""
        from config.config import Config
        self.driver.get(Config.BUTTONS_URL)
        self.logger.info(f"Navigated to buttons page: {Config.BUTTONS_URL}")
    
    def double_click_button(self):
        """Perform double click on double click button"""
        element = self.find_element(self.DOUBLE_CLICK_BUTTON)
        self.actions.double_click(element).perform()
        self.logger.info("Performed double click")
    
    def right_click_button(self):
        """Perform right click on right click button"""
        element = self.find_element(self.RIGHT_CLICK_BUTTON)
        self.actions.context_click(element).perform()
        self.logger.info("Performed right click")
    
    def click_dynamic_button(self):
        """Click on dynamic click button"""
        self.click(self.DYNAMIC_CLICK_BUTTON)
        self.logger.info("Performed dynamic click")
    
    def get_double_click_message(self):
        """
        Get double click message
        
        Returns:
            str: Double click message
        """
        return self.get_text(self.DOUBLE_CLICK_MESSAGE)
    
    def get_right_click_message(self):
        """
        Get right click message
        
        Returns:
            str: Right click message
        """
        return self.get_text(self.RIGHT_CLICK_MESSAGE)
    
    def get_dynamic_click_message(self):
        """
        Get dynamic click message
        
        Returns:
            str: Dynamic click message
        """
        return self.get_text(self.DYNAMIC_CLICK_MESSAGE)
    
    def is_double_click_message_displayed(self):
        """
        Check if double click message is displayed
        
        Returns:
            bool: True if message is displayed
        """
        return self.is_displayed(self.DOUBLE_CLICK_MESSAGE)
