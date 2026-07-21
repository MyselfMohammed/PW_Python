from playwright.sync_api import sync_playwright

import pytest

from config.config import Config


@pytest.fixture(scope="session")

def browser():

    with sync_playwright() as p:

        browser = p.chromium.launch(

            headless=Config.HEADLESS,

            slow_mo=300

        )

        yield browser

        browser.close()


@pytest.fixture()

def page(browser):

    context = browser.new_context()

    page = context.new_page()

    page.set_default_timeout(Config.TIMEOUT)

    yield page

    context.close()