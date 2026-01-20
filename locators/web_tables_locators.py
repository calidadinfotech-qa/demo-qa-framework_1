from selenium.webdriver.common.by import By

class WebTablesLocators:
    """Locators for Web Tables Page"""
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    
    # Registration Form Locators (Modal)
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    AGE_INPUT = (By.ID, "age")
    SALARY_INPUT = (By.ID, "salary")
    DEPARTMENT_INPUT = (By.ID, "department")
    SUBMIT_BUTTON = (By.ID, "submit")
    
    # Table Locators
    TABLE_ROWS = (By.CSS_SELECTOR, ".rt-tr-group")
    EDIT_BUTTONS = (By.CSS_SELECTOR, "span[title='Edit']")
    DELETE_BUTTONS = (By.CSS_SELECTOR, "span[title='Delete']")
