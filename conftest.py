from .pages.locators import LoginPageLocators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import faker
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: en, ru etc')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test...")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope='session')
def link_to():
    return "http://selenium1py.pythonanywhere.com"


@pytest.fixture(scope='session')
def link_to_product():
    return "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.fixture(scope='function')
def email():
    f = faker.Faker()
    email = f.email()
    return email


@pytest.fixture(scope='function')
def password():
    return str(int(time.time()) // 44) + "AVG"
