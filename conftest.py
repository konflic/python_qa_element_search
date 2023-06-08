import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.0.110:8081")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Downloads/drivers"))


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser == "chrome":
        # В selenium 4 рекомендуют использование такого подхода
        service = ChromiumService()
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FFService()
        driver = webdriver.Firefox(service=service)
    else:
        driver = webdriver.Safari()

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
