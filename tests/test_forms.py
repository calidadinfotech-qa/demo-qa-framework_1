"""
Practice Form Tests - Forms Section
"""
import pytest
from pages.forms_page import FormsPage
from utils.test_data import TestData


@pytest.mark.forms
def test_practice_form_submission(driver):
    """
    Test Case: Verify practice form submission
    
    Steps:
    1. Navigate to practice form page
    2. Fill all required form fields
    3. Submit the form
    4. Verify confirmation modal is displayed
    """
    # Arrange
    forms_page = FormsPage(driver)
    test_data = TestData.PRACTICE_FORM_DATA
    
    # Act
    forms_page.navigate_to_forms()
    forms_page.fill_practice_form(
        test_data["first_name"],
        test_data["last_name"],
        test_data["email"],
        test_data["gender"],
        test_data["mobile"],
        test_data["date_of_birth"],
        test_data["subjects"],
        test_data["hobbies"],
        test_data["current_address"]
    )
    
    # Assert
    assert forms_page.is_confirmation_displayed(), "Confirmation modal should be displayed after form submission"
    print(f"Practice form submitted successfully for {test_data['first_name']} {test_data['last_name']}")
