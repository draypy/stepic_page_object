from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_basket_is_empty(self):
        assert "Your basket is empty." in self.browser.find_element(
            *BasketPageLocators.EMPTY).text, "basket is not empty"
