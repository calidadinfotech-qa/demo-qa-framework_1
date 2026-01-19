"""
Login Page Object - Book Store Application Login Page
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for Login Page"""
    
    # Locators
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    ERROR_MESSAGE = (By.ID, "name")
    LOGOUT_BUTTON = (By.ID, "submit")
    
    def __init__(self, driver):
        """Initialize LoginPage"""
        super().__init__(driver)
    
    def navigate_to_login(self):
        """Navigate to login page"""
        from config.config import Config
        self.driver.get(Config.LOGIN_URL)
        self.logger.info(f"Navigated to login page: {Config.LOGIN_URL}")
    
    def enter_username(self, username):
        """
        Enter username
        
        Args:
            username (str): Username to enter
        """
        self.send_keys(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """
        Enter password
        
        Args:
            password (str): Password to enter
        """
        self.send_keys(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Click login button"""
        self.scroll_to_element(self.LOGIN_BUTTON)
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """
        Perform login action
        
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
        Check if login was successful
        
        Returns:
            bool: True if login successful
        """
        try:
            # Check if logout button is present (indicates successful login)
            return self.is_displayed(self.LOGOUT_BUTTON)
        except:
            return False
    
    def get_error_message(self):
        """
        Get error message if login fails
        
        Returns:
            str: Error message text
        """
        try:
            return self.get_text(self.ERROR_MESSAGE)
        except:
            return ""
