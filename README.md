# Test Automation Framework - DemoQA

A professional, maintainable test automation framework built from scratch using Python, Selenium WebDriver, and pytest. This framework demonstrates industry best practices including Page Object Model (POM), comprehensive reporting, and proper documentation.

## 📋 Table of Contents
- [Overview](#overview)
- [Framework Architecture](#framework-architecture)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running Tests](#running-tests)
- [Reports](#reports)
- [Framework Components](#framework-components)
- [Best Practices](#best-practices)
- [Interview Preparation Guide](#interview-preparation-guide)
- [Troubleshooting](#troubleshooting)

## 🎯 Overview

This framework automates testing for [DemoQA](https://demoqa.com/), covering 5 different pages with comprehensive test coverage:

1. **Login Page** - Book Store Application login
2. **Text Box Page** - Form submission and validation
3. **Buttons Page** - Button interactions (double-click, right-click)
4. **Web Tables Page** - Dynamic table management
5. **Practice Form Page** - Complex form with multiple field types

## 🏗️ Framework Architecture

```
Demo_1/
├── config/                     # Configuration management
│   ├── __init__.py
│   └── config.py              # Centralized configuration
├── pages/                      # Page Object Model
│   ├── __init__.py
│   ├── base_page.py           # Base page with common methods
│   ├── login_page.py          # Login page object
│   ├── text_box_page.py       # Text box page object
│   ├── buttons_page.py        # Buttons page object
│   ├── web_tables_page.py     # Web tables page object
│   └── forms_page.py          # Forms page object
├── tests/                      # Test cases
│   ├── __init__.py
│   ├── conftest.py            # Pytest fixtures & hooks
│   ├── test_login.py          # Login tests
│   ├── test_text_box.py       # Text box tests
│   ├── test_buttons.py        # Buttons tests
│   ├── test_web_tables.py     # Web tables tests
│   └── test_forms.py          # Forms tests
├── utils/                      # Utilities
│   ├── __init__.py
│   ├── driver_factory.py      # WebDriver management
│   ├── logger.py              # Logging utility
│   └── test_data.py           # Test data management
├── reports/                    # Test reports (auto-generated)
├── screenshots/                # Screenshots (auto-generated)
├── logs/                       # Log files (auto-generated)
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Pytest configuration
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

### Design Patterns Used

1. **Page Object Model (POM)** - Separates page structure from test logic
2. **Factory Pattern** - WebDriver creation (driver_factory.py)
3. **Singleton Pattern** - Configuration management
4. **DRY Principle** - Reusable methods in BasePage

## ✨ Features

- ✅ **Page Object Model** - Maintainable and scalable architecture
- ✅ **Multiple Browser Support** - Chrome, Firefox, Edge
- ✅ **Headless Mode** - For CI/CD integration
- ✅ **Explicit Waits** - Robust element handling
- ✅ **Dual Reporting** - HTML and Allure reports
- ✅ **Screenshot on Failure** - Automatic failure capture
- ✅ **Comprehensive Logging** - File and console logging
- ✅ **Test Data Management** - Centralized test data
- ✅ **Pytest Markers** - Organize and filter tests
- ✅ **Configurable Settings** - Easy configuration management

## 📦 Prerequisites

Before setting up the framework, ensure you have:

- **Python 3.8+** installed ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package manager)
- **Git** for version control
- **Chrome/Firefox/Edge** browser installed
- **Java 8+** (required for Allure reporting)

### Verify Installation

```bash
python --version
pip --version
git --version
java --version
```

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
cd /Users/apple/projects/Demo_1
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Install Allure (Optional but Recommended)

**macOS:**
```bash
brew install allure
```

**Windows:**
```bash
scoop install allure
```

**Linux:**
```bash
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

### Step 5: Verify Setup

```bash
pytest --version
allure --version
```

## 🧪 Running Tests

### Run All Tests

```bash
pytest tests/
```

### Run Specific Test File

```bash
pytest tests/test_text_box.py
```

### Run Tests with HTML Report

```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

### Run Tests with Allure Report

```bash
# Generate Allure results
pytest tests/ --alluredir=reports/allure-results

# View Allure report
allure serve reports/allure-results
```

### Run Tests by Marker

```bash
# Run only login tests
pytest tests/ -m login

# Run only element tests
pytest tests/ -m elements

# Run only form tests
pytest tests/ -m forms
```

### Run Tests in Headless Mode

Edit `config/config.py` and set:
```python
HEADLESS = True
```

Then run:
```bash
pytest tests/
```

### Run Tests with Different Browser

Edit `config/config.py` and change:
```python
BROWSER = "firefox"  # Options: chrome, firefox, edge
```

### Run Tests with Verbose Output

```bash
pytest tests/ -v
```

### Run Specific Test Case

```bash
pytest tests/test_text_box.py::test_text_box_form_submission -v
```

## 📊 Reports

### HTML Report

After running tests with `--html` flag, open the report:

```bash
open reports/report.html  # macOS
# or
start reports/report.html  # Windows
```

**HTML Report Features:**
- Test execution summary
- Pass/Fail status
- Execution time
- Error details
- Self-contained (includes CSS/JS)

### Allure Report

Allure provides interactive, detailed reports:

```bash
pytest tests/ --alluredir=reports/allure-results
allure serve reports/allure-results
```

**Allure Report Features:**
- Interactive dashboard
- Test execution trends
- Detailed test steps
- Screenshots on failure
- Historical data
- Categories and tags

## 🔧 Framework Components

### 1. Configuration (config/config.py)

Centralized configuration for:
- Base URLs
- Browser settings
- Timeouts
- Paths
- Test credentials

**Key Settings:**
```python
BASE_URL = "https://demoqa.com"
BROWSER = "chrome"
HEADLESS = False
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 15
```

### 2. Page Objects (pages/)

Each page has its own class with:
- **Locators** - Element identifiers
- **Methods** - Page interactions

**Example:**
```python
class TextBoxPage(BasePage):
    FULL_NAME_INPUT = (By.ID, "userName")
    
    def enter_full_name(self, name):
        self.send_keys(self.FULL_NAME_INPUT, name)
```

### 3. Base Page (pages/base_page.py)

Common methods used by all pages:
- `find_element()` - Find element with wait
- `click()` - Click with wait
- `send_keys()` - Type text
- `get_text()` - Get element text
- `is_displayed()` - Check visibility
- `take_screenshot()` - Capture screenshot
- `scroll_to_element()` - Scroll to element

### 4. WebDriver Factory (utils/driver_factory.py)

Manages WebDriver creation:
- Browser selection
- Headless mode
- Window management
- Timeout configuration

### 5. Test Data (utils/test_data.py)

Centralized test data:
- User credentials
- Form data
- Table records

### 6. Logging (utils/logger.py)

Comprehensive logging:
- File logging (logs/)
- Console logging
- Timestamped logs
- Multiple log levels

### 7. Pytest Configuration (pytest.ini)

Test execution settings:
- Test discovery patterns
- Markers
- Report options
- Logging configuration

### 8. Fixtures (tests/conftest.py)

Pytest fixtures:
- `driver` - WebDriver setup/teardown
- `setup_teardown` - Test preparation
- Screenshot on failure hook
- Directory creation

## 📚 Best Practices Implemented

### 1. Page Object Model
- Separates test logic from page structure
- Improves maintainability
- Reduces code duplication

### 2. Explicit Waits
- More reliable than implicit waits
- Handles dynamic content
- Reduces flaky tests

### 3. Logging
- Tracks test execution
- Helps debugging
- Provides audit trail

### 4. Configuration Management
- Centralized settings
- Easy environment switching
- No hardcoded values

### 5. Test Data Management
- Separates data from tests
- Easy data updates
- Supports data-driven testing

### 6. Error Handling
- Try-except blocks
- Meaningful error messages
- Screenshot on failure

### 7. Code Organization
- Clear folder structure
- Logical grouping
- Easy navigation

## 🎤 Interview Preparation Guide

### Key Talking Points

#### 1. Framework Architecture
**Question:** "Explain your framework architecture"

**Answer:**
"I've built a hybrid framework using Page Object Model with pytest. The architecture has clear separation of concerns:
- **Pages layer** contains page objects with locators and methods
- **Tests layer** contains test cases using page objects
- **Utils layer** provides utilities like WebDriver factory, logging, and test data
- **Config layer** manages all configuration settings

This architecture ensures maintainability, scalability, and follows SOLID principles."

#### 2. Page Object Model
**Question:** "Why did you use Page Object Model?"

**Answer:**
"POM provides several benefits:
- **Maintainability** - If UI changes, I only update the page object, not all tests
- **Reusability** - Page methods can be reused across multiple tests
- **Readability** - Tests are more readable and business-focused
- **Reduced duplication** - Common operations are centralized in BasePage

For example, my BasePage has common methods like `click()`, `send_keys()`, and `wait_for_element()` that all page objects inherit."

#### 3. Handling Dynamic Elements
**Question:** "How do you handle dynamic elements?"

**Answer:**
"I use explicit waits with Expected Conditions:
```python
element = self.wait.until(EC.element_to_be_clickable(locator))
```

This approach:
- Waits for specific conditions
- Has configurable timeout
- Throws clear exceptions
- More reliable than sleep()

I've configured explicit wait to 15 seconds in my config, which can be adjusted based on application performance."

#### 4. Reporting
**Question:** "What reporting mechanisms have you implemented?"

**Answer:**
"I've implemented dual reporting:

**HTML Reports (pytest-html):**
- Self-contained HTML file
- Easy to share
- Shows pass/fail status and execution time

**Allure Reports:**
- Interactive dashboard
- Test execution trends
- Detailed test steps
- Screenshots on failure
- Historical data for trend analysis

Additionally, I capture screenshots automatically on test failures using pytest hooks."

#### 5. Test Data Management
**Question:** "How do you manage test data?"

**Answer:**
"I use a centralized TestData class in utils/test_data.py:
- All test data in one place
- Easy to update
- Supports different data sets
- Can be extended to read from JSON/CSV/Excel
- Separates data from test logic

This makes the framework data-driven ready and easy to maintain."

#### 6. CI/CD Integration
**Question:** "How would you integrate this with CI/CD?"

**Answer:**
"The framework is CI/CD ready:
- **Headless mode** - Set HEADLESS=True in config
- **Command-line execution** - pytest tests/
- **Exit codes** - pytest returns proper exit codes
- **Reports** - HTML and Allure reports can be archived
- **Parallel execution** - Can add pytest-xdist for parallel runs
- **Docker support** - Can containerize with Selenium Grid

For Jenkins/GitHub Actions, I would:
1. Set up Python environment
2. Install dependencies
3. Run tests in headless mode
4. Publish reports
5. Send notifications"

#### 7. Challenges Faced
**Question:** "What challenges did you face?"

**Answer:**
"Key challenges and solutions:
1. **Dynamic elements** - Solved with explicit waits and proper locator strategies
2. **Test flakiness** - Implemented robust waits and retry mechanisms
3. **Maintainability** - Used POM to centralize changes
4. **Debugging** - Added comprehensive logging and screenshots
5. **Cross-browser testing** - Created WebDriver factory for browser abstraction"

#### 8. Agile Integration
**Question:** "How does this fit into Agile ceremonies?"

**Answer:**
"This framework supports Agile practices:
- **Sprint Planning** - Estimate automation effort for user stories
- **Daily Standups** - Report test execution status
- **Sprint Review** - Demo automated tests and reports
- **Sprint Retrospective** - Discuss framework improvements
- **CI/CD** - Automated tests run on every commit
- **Definition of Done** - Includes automated test coverage"

### Common Interview Questions

1. **What is your framework type?**
   - Hybrid framework using POM with pytest

2. **What design patterns did you use?**
   - Page Object Model, Factory Pattern, Singleton

3. **How do you handle waits?**
   - Explicit waits with Expected Conditions

4. **What is your locator strategy?**
   - Priority: ID > CSS > XPath, stored as tuples

5. **How do you handle test failures?**
   - Screenshot capture, detailed logging, retry mechanism

6. **What browsers do you support?**
   - Chrome, Firefox, Edge via WebDriver factory

7. **How do you organize tests?**
   - By functionality, using pytest markers

8. **What reporting tools do you use?**
   - pytest-html and Allure

9. **How do you manage configuration?**
   - Centralized config.py file

10. **How would you add parallel execution?**
    - Use pytest-xdist: `pytest -n 4`

## 🐛 Troubleshooting

### Common Issues

#### 1. WebDriver Not Found
**Error:** `WebDriver not found`

**Solution:**
```bash
pip install webdriver-manager
```
The framework uses webdriver-manager to auto-download drivers.

#### 2. Import Errors
**Error:** `ModuleNotFoundError`

**Solution:**
Ensure you're in the project root and virtual environment is activated:
```bash
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

#### 3. Tests Failing Due to Timeouts
**Solution:**
Increase timeouts in `config/config.py`:
```python
IMPLICIT_WAIT = 15
EXPLICIT_WAIT = 20
```

#### 4. Screenshot Directory Not Found
**Solution:**
Directories are auto-created, but you can manually create:
```bash
mkdir -p screenshots logs reports
```

#### 5. Allure Command Not Found
**Solution:**
Install Allure:
```bash
brew install allure  # macOS
```

#### 6. Browser Not Opening
**Solution:**
- Check browser is installed
- Try different browser in config
- Check for browser updates

## 📝 Git Workflow

### Initialize Repository

```bash
git init
git add .
git commit -m "Initial commit: Test automation framework"
```

### Create New Branch

```bash
git checkout -b feature/automation-framework
```

### Push to GitHub (Calidad Org)

```bash
git remote add origin <your-github-repo-url>
git push -u origin feature/automation-framework
```

**Note:** Push to a new branch, NOT main, as per requirements.

## 🎓 Learning Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [Allure Reports](https://docs.qameta.io/allure/)

## 📞 Support

For questions or issues:
1. Check this README
2. Review logs in `logs/`
3. Check screenshots in `screenshots/`
4. Review test reports in `reports/`

## 🏆 Framework Highlights

- ✅ **5 Pages Automated** - Login, Text Box, Buttons, Web Tables, Forms
- ✅ **5 Test Cases** - One per page as required
- ✅ **Professional Structure** - Industry-standard architecture
- ✅ **Comprehensive Documentation** - Detailed README and code comments
- ✅ **Dual Reporting** - HTML and Allure
- ✅ **Best Practices** - POM, explicit waits, logging, configuration management
- ✅ **Interview Ready** - Complete preparation guide included

---

**Built with ❤️ for QA Excellence**

*Framework Version: 1.0*  
*Last Updated: January 2026*
