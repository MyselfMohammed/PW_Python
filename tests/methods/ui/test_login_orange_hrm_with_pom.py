import pytest
from playwright.sync_api import Page, expect
from config.config import BASE_URL, USERNAME, PASSWORD

from pages.login_page_orangeHRM import LoginPage
from pages.home_page_orangeHRM import HomePage

@pytest.mark.smoke
def test_login_orange_hrm(page:Page) -> None :
    
    login_page = LoginPage(page)
    
    login_page.navigate(BASE_URL)
    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_button_login()
    
    home_page = HomePage(page)
    
    home_page.verify_home_page_loaded()
    home_page.click_tab_performance()
    home_page.click_tab_dashboard()

    
   