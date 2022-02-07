from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.check_button_add_to_basket()
    page.add_to_basket()
    page.check_text_adding_to_basket()
    page.check_price_book_equal_amount_basket()
