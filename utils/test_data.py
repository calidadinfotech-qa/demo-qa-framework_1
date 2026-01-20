"""
Test data management for the framework
"""


class TestData:
    """Class containing all test data used across different test cases"""
    
    # Login credentials to be used for login tests
    VALID_USER = {
        "username": "testuser",  # Valid username
        "password": "Test@123"   # Valid password
    }
    
    INVALID_USER = {
        "username": "invaliduser",  # Invalid username for negative testing
        "password": "wrongpass"     # Invalid password
    }
    
    # Text Box data for testing the Text Box form
    TEXT_BOX_DATA = {
        "full_name": "John Doe",  # Full name input
        "email": "john.doe@example.com",  # Email input
        "current_address": "123 Main Street, New York, NY 10001",  # Current address
        "permanent_address": "456 Oak Avenue, Los Angeles, CA 90001"  # Permanent address
    }
    
    # Web Table data for adding a new record in the Web Tables page
    WEB_TABLE_RECORD = {
        "first_name": "Jane",  # First name
        "last_name": "Smith",  # Last name
        "email": "jane.smith@example.com",  # Email address
        "age": "30",  # Age
        "salary": "75000",  # Salary
        "department": "QA"  # Department
    }
    
    # Practice Form data for the comprehensive student registration form
    PRACTICE_FORM_DATA = {
        "first_name": "Alice",  # First name
        "last_name": "Johnson",  # Last name
        "email": "alice.johnson@example.com",  # Email
        "gender": "Female",  # Gender (should match radio button value)
        "mobile": "1234567890",  # Mobile number (10 digits)
        "date_of_birth": "15 Jan 1995",  # Date of birth
        "subjects": "Maths",  # Subjects to select
        "hobbies": "Reading",  # Hobbies to check
        "current_address": "789 Pine Road, Chicago, IL 60601"  # Current address
    }
