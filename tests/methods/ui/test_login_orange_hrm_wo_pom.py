import re
from playwright.sync_api import expect

def test_google_search(page):
    
    try :
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        expect(page).to_have_title(re.compile("orangehrm", re.IGNORECASE))
        print(f'"{page.title()}" - has been Opened')
    except Exception as e:
         print(f"Page was not Opened. Error : {e}")