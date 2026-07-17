from playwright.sync_api import TimeoutError
from locators.common_locators import CommonLocators

class BasePage:

    def __init__(self, page):
        self.page = page

    def wait_for_spinner(self):
        spinner = self.page.locator(CommonLocators.SPINNER)

        if spinner.is_visible():
            try:
                spinner.wait_for(state="hidden", timeout=10000)
            except TimeoutError:
                raise AssertionError("Loading spinner did not disappear within 10 seconds.")