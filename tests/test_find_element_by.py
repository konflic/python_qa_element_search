import time

from selenium.webdriver.common.by import By


def test_login_page(browser):
    browser.get(browser.url)
    browser.find_element(value="_desktop_cart")
