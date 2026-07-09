
"""
| Scope      | Created                            | Destroyed                      | Runs                         |
| ---------- | ---------------------------------- | ------------------------------ | ---------------------------- |
| `session`  | Before all tests                   | After all tests                | Once for the entire test run |
| `function` | Before each test                   | After each test                | Every test function          |
| `class`    | Before first test in a class       | After last test in the class   | Once per class               |
| `module`   | Before first test in a Python file | After last test in the file    | Once per file                |
| `package`  | Before first test in a package     | After last test in the package | Once per package             |
"""

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()