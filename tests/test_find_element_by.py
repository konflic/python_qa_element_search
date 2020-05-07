import time


def test_login_page(browser):
    browser.get(browser.url + "/admin")
    browser.find_element_by_id("input-username")
    browser.find_element_by_name("password")
    browser.find_element_by_css_selector("button[type='submit']")
    browser.find_element_by_link_text("Forgotten Password")
    browser.find_element_by_xpath("//*[text()='OpenCart']")
    time.sleep(2) # Для демонстрации
