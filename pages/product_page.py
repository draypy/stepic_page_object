import time

from .base_page import BasePage
from .locators import ProductLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def check_button_add_to_basket(self):
        assert self.is_element_present(*ProductLocators.ADD_TO_BASKET), '"Add to basket button" is not implemented'

    def check_text_adding_to_basket(self):
        assert self.is_element_present(*ProductLocators.ADDED_TO_BASKET), 'Book didnt add to basket'

    def check_price_book_equal_amount_basket(self):
        book_price = self.browser.find_element(*ProductLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductLocators.BASKET_PRICE)
        assert book_price.text in basket_price.text, "smth went wrong"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductLocators.ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()

    def check_naming_product_and_basket_product(self):
        book_name = self.browser.find_element(*ProductLocators.PRODUCT_NAME)
        basket_book_name = self.browser.find_element(*ProductLocators.BASKET_PRODUCT_NAME)
        assert book_name.text == basket_book_name.text, "names are incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappear"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
