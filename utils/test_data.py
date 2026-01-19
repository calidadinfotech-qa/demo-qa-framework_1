"""
Test data management for the framework
"""


class TestData:
    """Class containing all test data"""
    
    # Login credentials
    VALID_USER = {
        "username": "testuser",
        "password": "Test@123"
    }
    
    INVALID_USER = {
        "username": "invaliduser",
        "password": "wrongpass"
    }
    
    # Text Box data
    TEXT_BOX_DATA = {
        "full_name": "John Doe",
        "email": "john.doe@example.com",
        "current_address": "123 Main Street, New York, NY 10001",
        "permanent_address": "456 Oak Avenue, Los Angeles, CA 90001"
    }
    
    # Web Table data
    WEB_TABLE_RECORD = {
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@example.com",
        "age": "30",
        "salary": "75000",
        "department": "QA"
    }
    
    # Practice Form data
    PRACTICE_FORM_DATA = {
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice.johnson@example.com",
        "gender": "Female",
        "mobile": "1234567890",
        "date_of_birth": "15 Jan 1995",
        "subjects": "Maths",
        "hobbies": "Reading",
        "current_address": "789 Pine Road, Chicago, IL 60601"
    }
