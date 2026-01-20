"""
Forms Page Object - Forms > Practice Form
Handles interactions with the Student Registration Form.
"""
from selenium.webdriver.common.by import By  # Element locator strategy
from selenium.webdriver.support.ui import Select  # For handling dropdowns (though not currently used as custom elements are handled differently)
from selenium.webdriver.common.keys import Keys  # For keyboard interactions (e.g., ENTER key)
from pages.base_page import BasePage  # Base class
from locators.forms_locators import FormsLocators


class FormsPage(BasePage):
    """Page Object for Practice Form Page. Handles complex form inputs including radio buttons, checkboxes, and date pickers."""
    
    
    def __init__(self, driver):
        """Initialize FormsPage"""
        super().__init__(driver)
    
    def navigate_to_forms(self):
        """
        Navigate to practice form page using URL from config.
        """
        from config.config import Config
        self.driver.get(Config.FORMS_URL)
        self.logger.info(f"Navigated to forms page: {Config.FORMS_URL}")
    
    def enter_first_name(self, first_name):
        """Enter first name into the field"""
        self.send_keys(FormsLocators.FIRST_NAME_INPUT, first_name)
    
    def enter_last_name(self, last_name):
        """Enter last name into the field"""
        self.send_keys(FormsLocators.LAST_NAME_INPUT, last_name)
    
    def enter_email(self, email):
        """Enter email into the field"""
        self.send_keys(FormsLocators.EMAIL_INPUT, email)
    
    def select_gender(self, gender):
        """
        Select gender radio button based on input string.
        
        Args:
            gender (str): Gender - Male, Female, or Other
        """
        if gender.lower() == "male":
            self.click(FormsLocators.GENDER_MALE)
        elif gender.lower() == "female":
            self.click(FormsLocators.GENDER_FEMALE)
        else:
            self.click(FormsLocators.GENDER_OTHER)
    
    def enter_mobile(self, mobile):
        """
        Enter mobile number. Note: Should be 10 digits.
        """
        self.send_keys(FormsLocators.MOBILE_INPUT, mobile)
    
    def enter_date_of_birth(self, date):
        """
        Enter date of birth.
        Uses keyboard shortcuts to select all and replace text, then hit Enter.
        
        Args:
            date (str): Date in format "DD MMM YYYY" (e.g., "15 Jan 1995")
        """
        self.click(FormsLocators.DATE_OF_BIRTH_INPUT)  # Focus the element
        element = self.find_element(FormsLocators.DATE_OF_BIRTH_INPUT)
        # Select existing text (Ctrl/Cmd + A) - using Control for simplicity, might need Command on Mac if not handled by driver
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(date) # Type new date
        element.send_keys(Keys.ENTER) # Confirm selection
    
    def enter_subjects(self, subjects):
        """
        Enter subjects into auto-complete field.
        Types the subject and hits Enter to select the first match.
        
        Args:
            subjects (str): Subject name
        """
        element = self.find_element(FormsLocators.SUBJECTS_INPUT)
        element.send_keys(subjects)
        element.send_keys(Keys.ENTER)
    
    def select_hobbies(self, hobby):
        """
        Select hobby checkbox based on input string.
        
        Args:
            hobby (str): Hobby - Sports, Reading, or Music
        """
        if hobby.lower() == "sports":
            self.click(FormsLocators.HOBBIES_SPORTS)
        elif hobby.lower() == "reading":
            self.click(FormsLocators.HOBBIES_READING)
        else:
            self.click(FormsLocators.HOBBIES_MUSIC)
    
    def enter_current_address(self, address):
        """Enter current address into textarea"""
        self.send_keys(FormsLocators.CURRENT_ADDRESS_INPUT, address)
    
    def click_submit(self):
        """
        Click submit button.
        Scrolls to element first to ensure it's not obscured by footer/ads.
        """
        self.scroll_to_element(FormsLocators.SUBMIT_BUTTON)
        self.click(FormsLocators.SUBMIT_BUTTON)
    
    def fill_practice_form(self, first_name, last_name, email, gender, mobile, 
                          date_of_birth, subjects, hobbies, current_address):
        """
        Wrapper method to fill the complete practice form.
        
        Args:
            first_name (str): First name
            last_name (str): Last name
            email (str): Email
            gender (str): Gender
            mobile (str): Mobile number
            date_of_birth (str): Date of birth
            subjects (str): Subjects
            hobbies (str): Hobbies
            current_address (str): Current address
        """
        self.logger.info("Filling practice form")
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.select_gender(gender)
        self.enter_mobile(mobile)
        self.enter_date_of_birth(date_of_birth)
        self.enter_subjects(subjects)
        self.select_hobbies(hobbies)
        self.enter_current_address(current_address)
        self.click_submit()
    
    def is_confirmation_displayed(self):
        """
        Check if confirmation modal is displayed after submission.
        
        Returns:
            bool: True if confirmation is displayed
        """
        return self.is_displayed(FormsLocators.CONFIRMATION_MODAL)
