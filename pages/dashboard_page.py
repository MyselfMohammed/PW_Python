from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.menu_pim = page.get_by_role("link", name="PIM")
        self.menu_dashboard = page.get_by_role("link", name="Dashboard")

    def open_pim(self):
        self.click(self.menu_pim)

    def verify_dashboard_loaded(self):
        self.assert_visible(self.menu_dashboard)