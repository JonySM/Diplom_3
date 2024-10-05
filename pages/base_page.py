import allure
from selenium.webdriver import ActionChains
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

    @allure.step('Ожидаем, что элемент пропадет на странице')
    def wait_text_element_changed(self, locator, text):
        WebDriverWait(self.driver, 30).until_not(expected_conditions.text_to_be_present_in_element(locator, text))

    @allure.step('Элемент присутствует на странице')
    def is_element_exist(self, locator) -> bool:
        try:
            WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        except Exception:
            return False
        return True

    @allure.step('Открываем страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Клик на элемент c помощью JS скрипта')
    def find_and_click_element(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Передвигаем элемент')
    def move_element(self, locator_source, locator_target):
        source_element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator_source))
        target_element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator_target))
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()




