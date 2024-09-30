import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    @allure.step('Создаем конструктор ')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем элемент на странице')
    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Открываем страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Клик на элемент c помощью JS скрипта')
    def find_and_click_element(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)


