from playwright.sync_api import Page
from config.config import URL_ORANGE_HRM

class LoginPage():
    
    def __init__(self, page:Page):
        self.page = page
        self.input_username = page.get_by_role("textbox", name = "username")
        self.input_password = page.get_by_role("textbox", name = "password")
        self.button_login = page.get_by_role("button", name = "login")
        
    def navigate(self):
        self.page.goto(URL_ORANGE_HRM)
        
    def enter_username(self, username:str):
        self.input_username.fill(username)
        
    def enter_password(self, password:str):
        self.input_password.fill(password)
        
    def click_button_login(self):
        self.button_login.click()
        
    def login(self, username:str, password:str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_button_login()
        
