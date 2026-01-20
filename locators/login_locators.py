from selenium.webdriver.common.by import By

class LoginLocators:
    """Locators for Login Page"""
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    ERROR_MESSAGE = (By.ID, "name")
    LOGOUT_BUTTON = (By.ID, "submit")  # Used to verify successful login
