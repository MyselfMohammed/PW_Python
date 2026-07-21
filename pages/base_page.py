from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        locator.wait_for(state="visible")
        locator.click()

    def fill(self, locator, value):
        locator.wait_for(state="visible")
        locator.fill(str(value))

    def type(self, locator, value):
        locator.wait_for(state="visible")
        locator.press_sequentially(str(value))

    def select_dropdown(self, locator, value):
        locator.select_option(value)

    def get_text(self, locator):
        return locator.text_content()

    def wait_visible(self, locator):
        locator.wait_for(state="visible")

    def wait_hidden(self, locator):
        locator.wait_for(state="hidden")

    def is_visible(self, locator):
        return locator.is_visible()

    def assert_text(self, locator, text):
        expect(locator).to_have_text(text)

    def assert_visible(self, locator):
        expect(locator).to_be_visible()

    def take_screenshot(self, path):
        self.page.screenshot(path=path, full_page=True)