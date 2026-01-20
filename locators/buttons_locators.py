from selenium.webdriver.common.by import By

class ButtonsLocators:
    """Locators for Buttons Page"""
    DOUBLE_CLICK_BUTTON = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.ID, "rightClickBtn")
    # Using xpath for dynamic button as ID might change or not differ significantly
    DYNAMIC_CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    
    # Message locators (success messages)
    DOUBLE_CLICK_MESSAGE = (By.ID, "doubleClickMessage")
    RIGHT_CLICK_MESSAGE = (By.ID, "rightClickMessage")
    DYNAMIC_CLICK_MESSAGE = (By.ID, "dynamicClickMessage")
