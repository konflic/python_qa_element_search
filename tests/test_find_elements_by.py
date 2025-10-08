import time

from selenium.webdriver.common.by import By


def test_main_page_menu(browser):
    time.sleep(1)  # Пауза для демонстрации
    browser.get(browser.url)
    menu_items = browser.find_elements(By.CSS_SELECTOR, "ul.top-menu > li")
    assert len(menu_items) == 7, "Неверное количество элементов меню"


def test_main_page_fetured_items(browser):
    time.sleep(1)  # Пауза для демонстрации
    browser.get(browser.url)
    fetured_items = browser.find_elements(By.CSS_SELECTOR, '[data-type="popularproducts"] .product')
    assert len(fetured_items) == 8, "Неверное количество продуктов в блоке popular"
