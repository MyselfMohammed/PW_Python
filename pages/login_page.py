from pages.base_page import BasePage
from config.config import Config


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.txt_username = page.locator("input[name='username']")
        self.txt_password = page.locator("input[name='password']")
        self.btn_login = page.locator("button[type='submit']")

    def open(self):
        self.navigate(Config.BASE_URL)

    def login(self):

        self.fill(self.txt_username, Config.USERNAME)

        self.fill(self.txt_password, Config.PASSWORD)

        self.click(self.btn_login)