from playwright.sync_api import Page

class LoginPage():
    
    def __init__(self, page:Page):
        self.page = page
        
        self.input_username = page.get_by_role("textbox", name = "Username")
        self.input_password = page.get_by_role("textbox", name = "Password")
        self.button_login = page.get_by_role("button", name = "Login")
        
        # self.input_username = page.locator('input[name="username"]')
        # self.input_password = page.locator('input[name="password"]')
        # self.button_login = page.get_by_role("button", name="Login")
    
    def navigate(self, url: str):
        self.page.goto(url)
    
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
        
