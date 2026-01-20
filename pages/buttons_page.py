"""
Buttons Page Object - Elements > Buttons
Handles interactions with different types of button clicks (double, right, dynamic).
"""
from selenium.webdriver.common.by import By  # For element location
from selenium.webdriver.common.action_chains import ActionChains  # For advanced actions like double click
from pages.base_page import BasePage  # Base class
from locators.buttons_locators import ButtonsLocators


class ButtonsPage(BasePage):
    """Page Object for Buttons Page. Contains locators and actions for button testing."""
    
    
    def __init__(self, driver):
        """Initialize ButtonsPage with driver and ActionChains"""
        super().__init__(driver)
        # ActionChains is needed for double click and context click (right click)
        self.actions = ActionChains(driver)
    
    def navigate_to_buttons(self):
        """
        Navigate to the buttons page.
        """
        from config.config import Config
        self.driver.get(Config.BUTTONS_URL)
        self.logger.info(f"Navigated to buttons page: {Config.BUTTONS_URL}")
    
    def double_click_button(self):
        """
        Perform a double click action on the double click button.
        """
        element = self.find_element(ButtonsLocators.DOUBLE_CLICK_BUTTON)
        # Use ActionChains to perform double click
        self.actions.double_click(element).perform()
        self.logger.info("Performed double click")
    
    def right_click_button(self):
        """
        Perform a right click (context click) action.
        """
        element = self.find_element(ButtonsLocators.RIGHT_CLICK_BUTTON)
        # Use ActionChains to perform context click
        self.actions.context_click(element).perform()
        self.logger.info("Performed right click")
    
    def click_dynamic_button(self):
        """
        Click on the dynamic button (simple click).
        """
        self.click(ButtonsLocators.DYNAMIC_CLICK_BUTTON)
        self.logger.info("Performed dynamic click")
    
    def get_double_click_message(self):
        """
        Get the success message displayed after double click.
        
        Returns:
            str: Message text
        """
        return self.get_text(ButtonsLocators.DOUBLE_CLICK_MESSAGE)
    
    def get_right_click_message(self):
        """
        Get the success message displayed after right click.
        
        Returns:
            str: Message text
        """
        return self.get_text(ButtonsLocators.RIGHT_CLICK_MESSAGE)
    
    def get_dynamic_click_message(self):
        """
        Get the success message displayed after dynamic click.
        
        Returns:
            str: Message text
        """
        return self.get_text(ButtonsLocators.DYNAMIC_CLICK_MESSAGE)
    
    def is_double_click_message_displayed(self):
        """
        Check if double click message is displayed.
        
        Returns:
            bool: True if displayed
        """
        return self.is_displayed(ButtonsLocators.DOUBLE_CLICK_MESSAGE)
