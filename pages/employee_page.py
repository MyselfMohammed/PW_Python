from pages.base_page import BasePage


class EmployeePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.btn_add = page.get_by_role("button", name="Add")
        self.first_name = page.locator("input[name='firstName']")
        self.last_name = page.locator("input[name='lastName']")
        self.employee_id = page.locator("xpath=(//input[contains(@class,'oxd-input')])[5]")
        self.btn_save = page.get_by_role("button", name="Save")

    def click_add_employee(self):
        self.click(self.btn_add)

    def create_employee(self, first_name, last_name, employee_id):
        self.fill(self.first_name, first_name)
        self.fill(self.last_name, last_name)
        self.employee_id.clear()
        self.fill(self.employee_id, employee_id)
        self.click(self.btn_save)
        
    def verify_employee_created(self, employee_id):
        self.page.wait_for_load_state("networkidle")
        employee_id_field = self.page.locator("xpath=(//input[contains(@class,'oxd-input')])[5]")
        employee_id_field.wait_for(state="visible")
        actual_id = employee_id_field.input_value()

        assert actual_id == employee_id,\
            f"Expected {employee_id}, Found {actual_id}"
            
    def wait_for_employee_list(self):
        self.page.wait_for_url("**/viewEmployeeList")
        self.btn_add.wait_for(state="visible")