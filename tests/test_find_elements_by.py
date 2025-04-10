import time

from selenium.webdriver.common.by import By


def test_main_page_menu(browser):
    time.sleep(1)  # Пауза для демонстрации
    browser.get(browser.url)
    menu_items = browser.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li")
    assert len(menu_items) == 8, "Неверное количество элементов меню"


def test_main_page_fetured_items(browser):
    time.sleep(1)  # Пауза для демонстрации
    browser.get(browser.url)
    fetured_items = browser.find_elements(By.CSS_SELECTOR, ".product-thumb")
    assert len(fetured_items) == 4, "Неверное количество продуктов в блоке featured"


def test_main_page_footer_blocks(browser):
    time.sleep(1)  # Пауза для демонстрации
    browser.get(browser.url)
    footer_blocks = browser.find_elements(By.XPATH, "//footer//ul")
    time.sleep(1)  # Пауза для демонстрации
    assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"


def test_main_page_open_product(browser):
    browser.get(browser.url)
    fetured_items = browser.find_elements(By.CLASS_NAME, "product-thumb")
    fetured_items[2].click()
    time.sleep(1)  # Пауза для демонстрации
