"""
Login Page Object - Book Store Application Login Page
Inherits from BasePage to leverage common functionality.
"""
from selenium.webdriver.common.by import By  # Import By class for locator strategies
from pages.base_page import BasePage  # Import BasePage class
from locators.login_locators import LoginLocators


class LoginPage(BasePage):
    """Page Object for Login Page. Contains locators and actions specific to the Login page."""
    
    def __init__(self, driver):
        """Initialize LoginPage and its base class"""
        super().__init__(driver)
    
    def navigate_to_login(self):
        """
        Navigate to the login page using the URL from config.
        """
        from config.config import Config  # Import locally to avoid circular import if any
        self.driver.get(Config.LOGIN_URL)
        self.logger.info(f"Navigated to login page: {Config.LOGIN_URL}")
    
    def enter_username(self, username):
        """
        Enter username into the username field.
        
        Args:
            username (str): Username to enter
        """
        self.send_keys(LoginLocators.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """
        Enter password into the password field.
        
        Args:
            password (str): Password to enter
        """
        self.send_keys(LoginLocators.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """
        Click the login button.
        Scrolls to element first to ensure it's in view.
        """
        self.scroll_to_element(LoginLocators.LOGIN_BUTTON)
        self.click(LoginLocators.LOGIN_BUTTON)
    
    def login(self, username, password):
        """
        Perform the complete login action:
        1. Enter username
        2. Enter password
        3. Click login button
        
        Args:
            username (str): Username
            password (str): Password
        """
        self.logger.info(f"Attempting login with username: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def is_login_successful(self):
        """
        Check if login was successful by looking for the logout button.
        
        Returns:
            bool: True if login successful (logout button is visible)
        """
        try:
            # Check if logout button is present (indicates successful login)
            return self.is_displayed(LoginLocators.LOGOUT_BUTTON)
        except:
            return False
    
    def get_error_message(self):
        """
        Get error message text if login fails.
        
        Returns:
            str: Error message text, or empty string if not found
        """
        try:
            return self.get_text(LoginLocators.ERROR_MESSAGE)
        except:
            return ""
