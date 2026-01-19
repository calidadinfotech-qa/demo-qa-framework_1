"""
Web Tables Page Object - Elements > Web Tables
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class WebTablesPage(BasePage):
    """Page Object for Web Tables Page"""
    
    # Locators
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    AGE_INPUT = (By.ID, "age")
    SALARY_INPUT = (By.ID, "salary")
    DEPARTMENT_INPUT = (By.ID, "department")
    SUBMIT_BUTTON = (By.ID, "submit")
    TABLE_ROWS = (By.CSS_SELECTOR, ".rt-tr-group")
    EDIT_BUTTONS = (By.CSS_SELECTOR, "span[title='Edit']")
    DELETE_BUTTONS = (By.CSS_SELECTOR, "span[title='Delete']")
    
    def __init__(self, driver):
        """Initialize WebTablesPage"""
        super().__init__(driver)
    
    def navigate_to_web_tables(self):
        """Navigate to web tables page"""
        from config.config import Config
        self.driver.get(Config.WEB_TABLES_URL)
        self.logger.info(f"Navigated to web tables page: {Config.WEB_TABLES_URL}")
    
    def click_add_button(self):
        """Click add new record button"""
        self.click(self.ADD_BUTTON)
    
    def enter_first_name(self, first_name):
        """Enter first name"""
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
    
    def enter_last_name(self, last_name):
        """Enter last name"""
        self.send_keys(self.LAST_NAME_INPUT, last_name)
    
    def enter_email(self, email):
        """Enter email"""
        self.send_keys(self.EMAIL_INPUT, email)
    
    def enter_age(self, age):
        """Enter age"""
        self.send_keys(self.AGE_INPUT, age)
    
    def enter_salary(self, salary):
        """Enter salary"""
        self.send_keys(self.SALARY_INPUT, salary)
    
    def enter_department(self, department):
        """Enter department"""
        self.send_keys(self.DEPARTMENT_INPUT, department)
    
    def click_submit(self):
        """Click submit button"""
        self.click(self.SUBMIT_BUTTON)
    
    def add_record(self, first_name, last_name, email, age, salary, department):
        """
        Add a new record to the table
        
        Args:
            first_name (str): First name
            last_name (str): Last name
            email (str): Email
            age (str): Age
            salary (str): Salary
            department (str): Department
        """
        self.logger.info(f"Adding new record: {first_name} {last_name}")
        self.click_add_button()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_age(age)
        self.enter_salary(salary)
        self.enter_department(department)
        self.click_submit()
    
    def get_table_rows_count(self):
        """
        Get count of table rows
        
        Returns:
            int: Number of rows
        """
        rows = self.find_elements(self.TABLE_ROWS)
        # Filter out empty rows
        non_empty_rows = [row for row in rows if row.text.strip()]
        return len(non_empty_rows)
    
    def is_record_added(self, email):
        """
        Check if a record with given email exists
        
        Args:
            email (str): Email to search for
            
        Returns:
            bool: True if record exists
        """
        try:
            locator = (By.XPATH, f"//div[@class='rt-td' and contains(text(), '{email}')]")
            return self.is_displayed(locator)
        except:
            return False
