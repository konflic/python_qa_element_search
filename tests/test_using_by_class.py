import time

from selenium.webdriver.common.by import By
from page_objects.LoginAdminPage import LoginAdminPage


def test_login_page(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(By.ID, "input-username")
    browser.find_element(By.NAME, "password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.LINK_TEXT, "Forgotten Password")
    browser.find_element(By.XPATH, "//*[text()='OpenCart']")
    time.sleep(2)  # Для демонстрации


def test_login_page_external(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON)
    browser.find_element(*LoginAdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*LoginAdminPage.OPENCART_LINK)
    time.sleep(2)  # Для демонстрации
