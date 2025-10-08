from selenium.webdriver.common.by import By


class LoginAdminPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.NAME, "passwd")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.PARTIAL_LINK_TEXT, "I forgot my password")
    STAY_LOGGED_IN = (By.XPATH, '//input[@name="stay_logged_in"]')
