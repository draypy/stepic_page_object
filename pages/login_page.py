from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'wrong link'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login Submit_link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_SUBMIT), "Register Submit_link is not presented"

    def register_new_user(self, email, password):
        login = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login.click()
        email_filed = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_filed.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit.click()


