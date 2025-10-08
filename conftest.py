import platform
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://localhost:8081/")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromiumService())
    elif browser_name == "firefox":
        if "24.04" in platform.version():
            service = FFService(executable_path="/snap/bin/geckodriver")
        else:
            service = FFService()
        driver = webdriver.Firefox(options=FFOptions(), service=service)
    else:
        driver = webdriver.Safari()

    driver.maximize_window()
    driver.url = url

    request.addfinalizer(driver.close)

    return driver
