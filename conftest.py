import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

from pages.lk_page import LkPage
from settings import Url, Data
from stellar_burger_api import StellarBurgersApi


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.maximize_window()
    elif request.param == 'firefox':
        browser = webdriver.Firefox(service=FirefoxService(r'C:\Users\e.sergeev\WebDriver\bin\geckodriver.exe'))
        browser.maximize_window()

    browser.get(Url.STELLAR_BURGERS_URL)

    yield browser

    browser.quit()

@allure.step('Фикстура создания случайного пользователя и последующее его удаление')
@pytest.fixture(scope='function')
def create_random_user():
    create_random_user = StellarBurgersApi.create_new_random_user()

    yield create_random_user
    accesstoken = create_random_user.json()['accessToken']
    StellarBurgersApi.delete_user(accesstoken)

@pytest.fixture
def authorization(driver, create_random_user):
    lk_page = LkPage(driver)
    lk_page.open_page(Url.STELLAR_BURGERS_URL)
    lk_page.click_on_the_login_button()
    user = create_random_user.json()['user']
    email = user['email']
    lk_page.set_email_for_login(email)
    lk_page.set_password_login(Data.CREATE_RANDOM_USER_BODY.get('password'))
    lk_page.click_on_the_login_main_button()



