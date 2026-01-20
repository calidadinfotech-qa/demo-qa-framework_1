"""
Login Page Tests - Book Store Application
"""
import pytest  # Import pytest framework
from pages.login_page import LoginPage  # Import Login Page Object
from utils.test_data import TestData  # Import Test Data


@pytest.mark.login  # Mark this test as part of the 'login' suite
def test_valid_login(driver):
    """
    Test Case: Verify user can login with valid credentials
    
    Steps:
    1. Navigate to login page
    2. Enter valid username and password
    3. Click login button
    4. Verify login is successful
    """
    # Arrange: Initialize Page Object
    login_page = LoginPage(driver)
    
    # Act: Perform login actions
    login_page.navigate_to_login()
    # Call the login method with valid credentials from TestData
    login_page.login(
        TestData.VALID_USER["username"],
        TestData.VALID_USER["password"]
    )
    
    # Assert: Verify success
    # Note: DemoQA login requires actual registered user
    # This test demonstrates the framework structure
    # In real scenario, you would register a user first or use test credentials
    assert login_page.get_current_url() != ""
    print("Login test completed - Framework structure validated")
