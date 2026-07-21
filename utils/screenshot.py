import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(page,
                test_name):

        os.makedirs("screenshots",
                    exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_name = f"screenshots/{test_name}_{timestamp}.png"

        page.screenshot(path=file_name,
                        full_page=True)

        return file_name