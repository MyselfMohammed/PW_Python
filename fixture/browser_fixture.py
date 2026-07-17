import pytest
from playwright.sync_api import sync_playwright
from config.config import HEADLESS, SLOW_MO, TIMEOUT

@pytest.fixture(scope="session")
def browser():
    print("***** CUSTOM BROWSER FIXTURE *****")
    
    with sync_playwright() as p:
        
        browser = p.chromium.launch(
            headless=HEADLESS,
            slow_mo=SLOW_MO,
            args=["--start-maximized"]
        ) 
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(viewport=None)
    context.set_default_timeout(TIMEOUT)
    page = context.new_page()
    
    yield page
    
    context.close()