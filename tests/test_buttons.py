"""
Buttons Page Tests - Elements Section
"""
import pytest
from pages.buttons_page import ButtonsPage


@pytest.mark.elements
def test_double_click_button(driver):
    """
    Test Case: Verify double click button functionality
    
    Steps:
    1. Navigate to buttons page
    2. Perform double click on double click button
    3. Verify double click message is displayed
    """
    # Arrange
    buttons_page = ButtonsPage(driver)
    
    # Act
    buttons_page.navigate_to_buttons()
    buttons_page.double_click_button()
    
    # Assert
    assert buttons_page.is_double_click_message_displayed(), "Double click message should be displayed"
    message = buttons_page.get_double_click_message()
    assert "double" in message.lower(), "Message should contain 'double'"
    print(f"Double click successful. Message: {message}")
