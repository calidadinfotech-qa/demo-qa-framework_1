"""
Web Tables Page Tests - Elements Section
"""
import pytest  # Import pytest
from pages.web_tables_page import WebTablesPage  # Import Page Object
from utils.test_data import TestData  # Import Test Data


@pytest.mark.elements  # Mark as 'elements' suite
def test_add_new_record(driver):
    """
    Test Case: Verify adding a new record to web table
    
    Steps:
    1. Navigate to web tables page
    2. Get initial row count
    3. Add a new record
    4. Verify record is added successfully (count increases and data is visible)
    """
    # Arrange: Initialize Page Object and Test Data
    web_tables_page = WebTablesPage(driver)
    test_data = TestData.WEB_TABLE_RECORD
    
    # Act: Perform actions
    web_tables_page.navigate_to_web_tables()
    # Get current number of records for comparison
    initial_count = web_tables_page.get_table_rows_count()
    
    # Add record using the helper method
    web_tables_page.add_record(
        test_data["first_name"],
        test_data["last_name"],
        test_data["email"],
        test_data["age"],
        test_data["salary"],
        test_data["department"]
    )
    
    # Assert: Verify the result
    # Check if the email is visible in the table
    assert web_tables_page.is_record_added(test_data["email"]), \
        f"Record with email {test_data['email']} should be added to table"
    
    # Check if the row count increased
    final_count = web_tables_page.get_table_rows_count()
    assert final_count > initial_count, "Table row count should increase after adding record"
    print(f"Record added successfully: {test_data['first_name']} {test_data['last_name']}")
