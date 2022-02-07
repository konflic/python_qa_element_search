import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Downloads/drivers"))


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        # В selenium 4 рекомендуют использование такого подхода
        service = ChromiumService(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    else:
        driver = webdriver.Safari()

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
