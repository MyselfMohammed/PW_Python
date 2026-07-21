import allure
import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.employee_page import EmployeePage

from utils.csv_reader import CSVReader
from utils.csv_writer import CSVWriter
from utils.logger import logger
from utils.screenshot import Screenshot

CSV_FILE = "testdata/employees.csv"


@allure.feature("Employee Creation")
@allure.story("Data Driven Employee Creation")
class TestEmployeeCreation:

    @pytest.mark.regression
    def test_create_employee(self, page):

        login = LoginPage(page)
        dashboard = DashboardPage(page)
        employee = EmployeePage(page)

        # ==========================
        # Login ONLY ONCE
        # ==========================
        with allure.step("Open Application"):
            login.open()

        with allure.step("Login"):
            login.login()

        with allure.step("Verify Dashboard"):
            dashboard.verify_dashboard_loaded()

        logger.info("Login Successful")

        # ==========================
        # Read CSV
        # ==========================
        records = CSVReader.read_csv(CSV_FILE)

        for record in records:

            employee_id = record["EmployeeId"]

            # Skip records already processed
            if record["Status"].upper() == "SUCCESS":
                logger.info(f"{employee_id} already processed. Skipping.")
                continue

            logger.info("=" * 60)
            logger.info(f"Processing Employee : {employee_id}")

            try:

                # =====================================
                # Always navigate back to Employee List
                # =====================================

                with allure.step("Navigate to PIM"):
                    dashboard.open_pim()

                # Optional
                employee.wait_for_employee_list()

                with allure.step("Click Add Employee"):
                    employee.click_add_employee()

                with allure.step("Create Employee"):
                    employee.create_employee(record["FirstName"],record["LastName"],employee_id)

                # =====================================
                # Verify Employee Created
                # =====================================

                with allure.step("Verify Employee Creation"):
                    employee.verify_employee_created(employee_id)

                # =====================================
                # Update CSV
                # =====================================

                CSVWriter.update_status(CSV_FILE,employee_id,"SUCCESS")
                logger.info(f"{employee_id} Created Successfully")

            except Exception as e:

                logger.error(f"{employee_id} Failed")
                logger.error(str(e))

                screenshot = Screenshot.capture(page,employee_id)
                CSVWriter.update_status(CSV_FILE,employee_id,"FAILED")
                allure.attach(str(e),name="Failure Reason",attachment_type=allure.attachment_type.TEXT)

                with open(screenshot, "rb") as image:
                    allure.attach(
                        image.read(),
                        name=f"{employee_id}_Screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )

                # Continue with next employee
                continue

        logger.info("All Employees Processed Successfully")