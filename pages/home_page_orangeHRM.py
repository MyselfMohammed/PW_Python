from playwright.sync_api import Page, expect

class HomePage:
    
    def __init__(self, page:Page):
        self.page = Page
        self.button_upgrade = page.get_by_role("button", name="Upgrade")
        self.tab_performance = page.get_by_role("link", name="Performance")
        self.tab_dashboard = page.get_by_role("link", name="Dashboard")
        
    def is_button_upgrade_visible(self):
        expect(self.button_upgrade).to_be_visible()
        
    def click_tab_performance(self):
        self.tab_performance.click()
        
    def click_tab_dashboard(self):
        self.tab_dashboard.click()

    

     