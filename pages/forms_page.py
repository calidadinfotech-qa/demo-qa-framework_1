"""
Forms Page Object - Forms > Practice Form
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class FormsPage(BasePage):
    """Page Object for Practice Form Page"""
    
    # Locators
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    GENDER_MALE = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    GENDER_OTHER = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    MOBILE_INPUT = (By.ID, "userNumber")
    DATE_OF_BIRTH_INPUT = (By.ID, "dateOfBirthInput")
    SUBJECTS_INPUT = (By.ID, "subjectsInput")
    HOBBIES_SPORTS = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    HOBBIES_READING = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']")
    HOBBIES_MUSIC = (By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    CONFIRMATION_MODAL = (By.CLASS_NAME, "modal-content")
    CLOSE_MODAL_BUTTON = (By.ID, "closeLargeModal")
    
    def __init__(self, driver):
        """Initialize FormsPage"""
        super().__init__(driver)
    
    def navigate_to_forms(self):
        """Navigate to practice form page"""
        from config.config import Config
        self.driver.get(Config.FORMS_URL)
        self.logger.info(f"Navigated to forms page: {Config.FORMS_URL}")
    
    def enter_first_name(self, first_name):
        """Enter first name"""
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
    
    def enter_last_name(self, last_name):
        """Enter last name"""
        self.send_keys(self.LAST_NAME_INPUT, last_name)
    
    def enter_email(self, email):
        """Enter email"""
        self.send_keys(self.EMAIL_INPUT, email)
    
    def select_gender(self, gender):
        """
        Select gender
        
        Args:
            gender (str): Gender - Male, Female, or Other
        """
        if gender.lower() == "male":
            self.click(self.GENDER_MALE)
        elif gender.lower() == "female":
            self.click(self.GENDER_FEMALE)
        else:
            self.click(self.GENDER_OTHER)
    
    def enter_mobile(self, mobile):
        """Enter mobile number"""
        self.send_keys(self.MOBILE_INPUT, mobile)
    
    def enter_date_of_birth(self, date):
        """
        Enter date of birth
        
        Args:
            date (str): Date in format "DD MMM YYYY" (e.g., "15 Jan 1995")
        """
        self.click(self.DATE_OF_BIRTH_INPUT)
        element = self.find_element(self.DATE_OF_BIRTH_INPUT)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(date)
        element.send_keys(Keys.ENTER)
    
    def enter_subjects(self, subjects):
        """
        Enter subjects
        
        Args:
            subjects (str): Subject name
        """
        element = self.find_element(self.SUBJECTS_INPUT)
        element.send_keys(subjects)
        element.send_keys(Keys.ENTER)
    
    def select_hobbies(self, hobby):
        """
        Select hobby
        
        Args:
            hobby (str): Hobby - Sports, Reading, or Music
        """
        if hobby.lower() == "sports":
            self.click(self.HOBBIES_SPORTS)
        elif hobby.lower() == "reading":
            self.click(self.HOBBIES_READING)
        else:
            self.click(self.HOBBIES_MUSIC)
    
    def enter_current_address(self, address):
        """Enter current address"""
        self.send_keys(self.CURRENT_ADDRESS_INPUT, address)
    
    def click_submit(self):
        """Click submit button"""
        self.scroll_to_element(self.SUBMIT_BUTTON)
        self.click(self.SUBMIT_BUTTON)
    
    def fill_practice_form(self, first_name, last_name, email, gender, mobile, 
                          date_of_birth, subjects, hobbies, current_address):
        """
        Fill the complete practice form
        
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
        Check if confirmation modal is displayed
        
        Returns:
            bool: True if confirmation is displayed
        """
        return self.is_displayed(self.CONFIRMATION_MODAL)
