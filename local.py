import allure


@allure.step('Клик на элемент c помощью JS скрипта')
def find_and_click_element(self, locator):
    element = self.driver.find_element(*locator)
    self.driver.execute_script("arguments[0].click();", element)