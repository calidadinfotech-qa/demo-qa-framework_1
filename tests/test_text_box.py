"""
Text Box Page Tests - Elements Section
"""
import pytest  # Import pytest
from pages.text_box_page import TextBoxPage  # Import Page Object
from utils.test_data import TestData  # Import Test Data

@pytest.mark.elements  # Mark this test as part of the 'elements' suite
def test_text_box_form_submission(driver):
    """
    Test Case: Verify text box form submission and output display
    
    Steps:
    1. Navigate to text box page
    2. Fill all form fields
    3. Click submit button
    4. Verify output is displayed with correct data
    """
    # Arrange: Initialize Page Object and Test Data
    text_box_page = TextBoxPage(driver)
    test_data = TestData.TEXT_BOX_DATA
    
    # Act: Perform actions
    text_box_page.navigate_to_text_box()
    # Fill the form using data from TestData
    text_box_page.fill_form(
        test_data["full_name"],
        test_data["email"],
        test_data["current_address"],
        test_data["permanent_address"]
    )
    # Assert: Verify the result
    assert text_box_page.is_output_displayed(), "Output should be displayed after form submission"
    # Verify the content of the output matches input
    output_text = text_box_page.get_output_text()
    assert test_data["full_name"] in output_text, "Full name should be in output"
    assert test_data["email"] in output_text, "Email should be in output"
    print(f"Text box form submitted successfully. Output: {output_text}")
