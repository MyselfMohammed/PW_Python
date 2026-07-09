import re
from playwright.sync_api import expect

def test_google_search(page):
    page.wait_for_timeout(5000)
    page.goto("https://www.google.com/ncr")
    
    try:
        page.get_by_role("button", name="Aceept All").click(timeout=5000)
        print("Popups Appeared and Aceepted/Ignored")
    except:
        page.get_by_role("combobox", name="Search").fill("Playwright Python")
        page.keyboard.press("Enter")
        
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))