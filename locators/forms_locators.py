from selenium.webdriver.common.by import By

class FormsLocators:
    """Locators for Forms Page"""
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    
    # Gender radio buttons - using CSS selector on the label because the input itself might be hidden/obscured
    GENDER_MALE = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_OTHER = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    
    MOBILE_INPUT = (By.ID, "userNumber")
    DATE_OF_BIRTH_INPUT = (By.ID, "dateOfBirthInput")
    
    # Subjects is an auto-complete field
    SUBJECTS_INPUT = (By.ID, "subjectsInput")
    
    # Hobbies checkboxes
    HOBBIES_SPORTS = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_READING = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_MUSIC = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    
    # Modal that appears after successful submission
    CONFIRMATION_MODAL = (By.CLASS_NAME, "modal-content")
    CLOSE_MODAL_BUTTON = (By.ID, "closeLargeModal")
