"""
Text Box Page Object - Elements > Text Box
Handles the interaction with the Text Box section of the application.
"""
from selenium.webdriver.common.by import By  # Import By class for locator strategies
from pages.base_page import BasePage  # Import BasePage class
from locators.text_box_locators import TextBoxLocators


class TextBoxPage(BasePage):
    """Page Object for Text Box Page. Contains locators and actions specific to the Text Box form."""
    
    
    def __init__(self, driver):
        """Initialize TextBoxPage with the driver"""
        super().__init__(driver)
    
    def navigate_to_text_box(self):
        """
        Navigate to the text box page using the URL from config.
        """
        from config.config import Config
        self.driver.get(Config.TEXT_BOX_URL)
        self.logger.info(f"Navigated to text box page: {Config.TEXT_BOX_URL}")
    
    def enter_full_name(self, name):
        """
        Enter full name into field.
        
        Args:
            name (str): Full name value
        """
        self.send_keys(TextBoxLocators.FULL_NAME_INPUT, name)
    
    def enter_email(self, email):
        """
        Enter email into field.
        
        Args:
            email (str): Email value
        """
        self.send_keys(TextBoxLocators.EMAIL_INPUT, email)
    
    def enter_current_address(self, address):
        """
        Enter current address into textarea.
        
        Args:
            address (str): Address value
        """
        self.send_keys(TextBoxLocators.CURRENT_ADDRESS_INPUT, address)
    
    def enter_permanent_address(self, address):
        """
        Enter permanent address into textarea.
        
        Args:
            address (str): Address value
        """
        self.send_keys(TextBoxLocators.PERMANENT_ADDRESS_INPUT, address)
    
    def click_submit(self):
        """
        Click the submit button.
        Scrolls to element first to ensure visibility.
        """
        self.scroll_to_element(TextBoxLocators.SUBMIT_BUTTON)
        self.click(TextBoxLocators.SUBMIT_BUTTON)
    
    def fill_form(self, full_name, email, current_address, permanent_address):
        """
        Fill the complete text box form with provided data.
        
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
        Check if the output area is displayed after submission.
        
        Returns:
            bool: True if output is displayed, False otherwise
        """
        return self.is_displayed(TextBoxLocators.OUTPUT_BOX)
    
    def get_output_text(self):
        """
        Get the complete text content of the output area.
        
        Returns:
            str: Output text if displayed, empty string otherwise
        """
        if self.is_output_displayed():
            return self.get_text(TextBoxLocators.OUTPUT_BOX)
        return ""
