"""
Text Box Page Object - Elements > Text Box
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    """Page Object for Text Box Page"""
    
    # Locators
    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    OUTPUT_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p#currentAddress")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p#permanentAddress")
    OUTPUT_BOX = (By.ID, "output")
    
    def __init__(self, driver):
        """Initialize TextBoxPage"""
        super().__init__(driver)
    
    def navigate_to_text_box(self):
        """Navigate to text box page"""
        from config.config import Config
        self.driver.get(Config.TEXT_BOX_URL)
        self.logger.info(f"Navigated to text box page: {Config.TEXT_BOX_URL}")
    
    def enter_full_name(self, name):
        """Enter full name"""
        self.send_keys(self.FULL_NAME_INPUT, name)
    
    def enter_email(self, email):
        """Enter email"""
        self.send_keys(self.EMAIL_INPUT, email)
    
    def enter_current_address(self, address):
        """Enter current address"""
        self.send_keys(self.CURRENT_ADDRESS_INPUT, address)
    
    def enter_permanent_address(self, address):
        """Enter permanent address"""
        self.send_keys(self.PERMANENT_ADDRESS_INPUT, address)
    
    def click_submit(self):
        """Click submit button"""
        self.scroll_to_element(self.SUBMIT_BUTTON)
        self.click(self.SUBMIT_BUTTON)
    
    def fill_form(self, full_name, email, current_address, permanent_address):
        """
        Fill the complete text box form
        
        Args:
            full_name (str): Full name
            email (str): Email address
            current_address (str): Current address
            permanent_address (str): Permanent address
        """
        self.logger.info("Filling text box form")
        self.enter_full_name(full_name)
        self.enter_email(email)
        self.enter_current_address(current_address)
        self.enter_permanent_address(permanent_address)
        self.click_submit()
    
    def is_output_displayed(self):
        """
        Check if output is displayed
        
        Returns:
            bool: True if output is displayed
        """
        return self.is_displayed(self.OUTPUT_BOX)
    
    def get_output_text(self):
        """
        Get the complete output text
        
        Returns:
            str: Output text
        """
        if self.is_output_displayed():
            return self.get_text(self.OUTPUT_BOX)
        return ""
