import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach

DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='120.0'
    )


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "120.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    load_dotenv()
    remote_drv = os.getenv('REMOTE_DRV')
    driver = webdriver.Remote(command_executor=f'{remote_drv}', options=options)
    browser.config.base_url = "https://ostrovok.ru/"
    browser.config.driver = driver
    browser.config.driver_options = options

    browser.config.timeout = 4.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    #attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
