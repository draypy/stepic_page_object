from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser, link_to):
        browser.get(link_to)
        login_link = browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def test_guest_should_see_login_link(self, browser, link_to):
        browser.get(link_to)
        assert browser.find_element(*MainPageLocators.LOGIN_LINK), "smth went wrong"
