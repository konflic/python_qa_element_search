from selenium.webdriver.common.by import By

from locators import MainPage
from selenium.webdriver.common.action_chains import ActionChains


def test_element_by_class_name_selector(parametrize_browser):
    bro = parametrize_browser
    bro.find_element_by_class_name(MainPage.promoblock).click()
    bro.find_element_by_class_name("breadcrumb")


def test_element_by_xpath(browser):
    browser.find_element_by_xpath("//div[@class='swiper-viewport']").click()
    browser.find_element_by_xpath("//*[@class='breadcrumb']")
    browser.find_element_by_xpath("//button[@data-original-title='Add to Wish List']").click()
    browser.find_element_by_xpath("//div[contains(@class, 'alert-success')]")


def test_element_by_id(browser):
    browser.find_element(By.ID, "slideshow0").click()
    browser.find_element(By.CLASS_NAME, "breadcrumb")


def test_element_by_link_text(browser):
    desktops_link = browser.find_element_by_link_text("Desktops")
    ActionChains(browser).move_to_element(desktops_link).pause(2).perform()
    browser.find_element_by_link_text("Show All Desktops").click()
    browser.find_element_by_partial_link_text("Product Compare")


def test_elements_by_css_selector(browser):
    navbar_items = browser.find_elements(MainPage.nav_links)
    for item in navbar_items:
        ActionChains(browser).move_to_element(item).pause(0.5).perform()


# def test_element_by_class_name_selector(parametrize_browser):
#     parametrize_browser.find_element_by_class_name("swiper-viewport").click()
#     parametrize_browser.find_element_by_class_name("breadcrumb")
