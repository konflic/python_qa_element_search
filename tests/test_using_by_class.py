from pages import LoginAdminPage


def test_login_page_external(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON)
    browser.find_element(*LoginAdminPage.OPENCART_LINK)
