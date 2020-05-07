import time

# TODO: Улучшить строку импорта через локальный импорт внутри пакета
from locators.LoginAdminPage import LoginAdminPage


def test_login_page(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON)
    browser.find_element(*LoginAdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*LoginAdminPage.OPENCART_LINK)
    time.sleep(2)  # Для демонстрации


# TODO: Перевести на импорт локаторов тесты на главную страницу
def test_main_page_menu(browser):
    time.sleep(1)  # Пауза для демонстрации
    menu_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
    assert len(menu_items) == 8, "Неверное количество элементов меню"


def test_main_page_fetured_items(browser):
    time.sleep(1)  # Пауза для демонстрации
    fetured_items = browser.find_elements_by_class_name("product-thumb")
    assert len(fetured_items) == 4, "Неверное количество продуктов в блоке featured"


def test_main_page_footer_blocks(browser):
    time.sleep(1)  # Пауза для демонстрации
    footer_blocks = browser.find_elements_by_xpath("//footer//ul")
    result = footer_blocks[0].location_once_scrolled_into_view
    time.sleep(1)  # Пауза для демонстрации
    assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"
