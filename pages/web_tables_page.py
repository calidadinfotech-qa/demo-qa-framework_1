"""
Web Tables Page Object - Elements > Web Tables
Handles interactions with the Web Tables to add, edit, or delete records.
"""
from selenium.webdriver.common.by import By  # Element locator strategy
from pages.base_page import BasePage  # Base class
from locators.web_tables_locators import WebTablesLocators


class WebTablesPage(BasePage):
    """Page Object for Web Tables Page. Contains methods to manage table records."""
    
    
    def __init__(self, driver):
        """Initialize WebTablesPage"""
        super().__init__(driver)
    
    def navigate_to_web_tables(self):
        """
        Navigate to web tables page using URL from config.
        """
        from config.config import Config
        self.driver.get(Config.WEB_TABLES_URL)
        self.logger.info(f"Navigated to web tables page: {Config.WEB_TABLES_URL}")
    
    def click_add_button(self):
        """Click add new record button to open the modal"""
        self.click(WebTablesLocators.ADD_BUTTON)
    
    def enter_first_name(self, first_name):
        """Enter first name into modal field"""
        self.send_keys(WebTablesLocators.FIRST_NAME_INPUT, first_name)
    
    def enter_last_name(self, last_name):
        """Enter last name into modal field"""
        self.send_keys(WebTablesLocators.LAST_NAME_INPUT, last_name)
    
    def enter_email(self, email):
        """Enter email into modal field"""
        self.send_keys(WebTablesLocators.EMAIL_INPUT, email)
    
    def enter_age(self, age):
        """Enter age into modal field"""
        self.send_keys(WebTablesLocators.AGE_INPUT, age)
    
    def enter_salary(self, salary):
        """Enter salary into modal field"""
        self.send_keys(WebTablesLocators.SALARY_INPUT, salary)
    
    def enter_department(self, department):
        """Enter department into modal field"""
        self.send_keys(WebTablesLocators.DEPARTMENT_INPUT, department)
    
    def click_submit(self):
        """Click submit button to save the record"""
        self.click(WebTablesLocators.SUBMIT_BUTTON)
    
    def add_record(self, first_name, last_name, email, age, salary, department):
        """
        Complete flow to add a new record to the table.
        
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
        Get the number of non-empty rows in the table.
        
        Returns:
            int: Number of rows with data
        """
        rows = self.find_elements(WebTablesLocators.TABLE_ROWS)
        # Filter out empty rows (table usually has fixed 10 rows, some empty)
        non_empty_rows = [row for row in rows if row.text.strip()]
        return len(non_empty_rows)
    
    def is_record_added(self, email):
        """
        Check if a record with the given email exists in the table.
        
        Args:
            email (str): Email to search for
            
        Returns:
            bool: True if record exists, False otherwise
        """
        try:
            # Construct xpath to find a cell containing the email
            locator = (By.XPATH, f"//div[@class='rt-td' and contains(text(), '{email}')]")
            return self.is_displayed(locator)
        except:
            return False
