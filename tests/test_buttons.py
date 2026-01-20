"""
Buttons Page Tests - Elements Section
"""
import pytest  # Import pytest framework
from pages.buttons_page import ButtonsPage  # Import Page Object


@pytest.mark.elements  # Mark this test as part of the 'elements' suite
def test_double_click_button(driver):
    """
    Test Case: Verify double click button functionality
    
    Steps:
    1. Navigate to buttons page
    2. Perform double click on double click button
    3. Verify double click message is displayed
    """
    # Arrange: Initialize Page Object
    buttons_page = ButtonsPage(driver)
    
    # Act: Perform actions
    buttons_page.navigate_to_buttons()  # Go to the page
    buttons_page.double_click_button()  # Double click the button
    
    # Assert: Verify the result
    # Check if the success message is displayed
    assert buttons_page.is_double_click_message_displayed(), "Double click message should be displayed"
    
    # Check the text of the message
    message = buttons_page.get_double_click_message()
    assert "double" in message.lower(), "Message should contain 'double'"
    print(f"Double click successful. Message: {message}")
