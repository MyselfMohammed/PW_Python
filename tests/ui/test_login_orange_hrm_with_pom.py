from playwright.sync_api import Page, expect
from pages.login_page_orangeHRM import LoginPage
from pages.home_page_orangeHRM import HomePage

def test_login_orange_hrm(page:Page) -> None :
    login_page = LoginPage(page)
    home_page = HomePage(page)
    
    login_page.navigate()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_button_login()
    
    home_page.is_button_upgrade_visible()
    home_page.click_tab_performance()
    home_page.click_tab_dashboard()
    
   