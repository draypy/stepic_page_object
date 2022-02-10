from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators:
    EMPTY = (By.CSS_SELECTOR, "div#content_inner")


class LoginPageLocators:
    LOGIN_SUBMIT = (By.NAME, "login_submit")
    REGISTER_SUBMIT = (By.NAME, 'registration_submit')
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")


class ProductLocators:
    ADD_TO_BASKET = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    ADDED_TO_BASKET = (By.XPATH, '//div[@class="alertinner "]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner  > p > strong")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner  > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alerinner ')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_BTN = (By.CSS_SELECTOR, "span.btn-group")
