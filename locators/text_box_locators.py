from selenium.webdriver.common.by import By

class TextBoxLocators:
    """Locators for Text Box Page"""
    FULL_NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    
    # Output locators (displayed after form submission)
    OUTPUT_NAME = (By.ID, "name")
    OUTPUT_EMAIL = (By.ID, "email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p#currentAddress")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p#permanentAddress")
    OUTPUT_BOX = (By.ID, "output")
