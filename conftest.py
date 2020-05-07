import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="opera")
    parser.addoption("--url", action="store", default="https://demo.opencart.com/")


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    # Инициализация нужного объекта
    drivers = "/Users/mikhail/Downloads/drivers"
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=drivers + "/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=drivers + "/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    else:
        driver = webdriver.Safari()
    # Предварительная настройка запуска
    driver.maximize_window()
    request.addfinalizer(driver.close)
    driver.get(url)
    # Сохраняю ссылку на базовый url
    driver.url = url
    # Выдача драйвера из фикстуры
    return driver
