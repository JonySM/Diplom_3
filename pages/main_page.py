import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Клик на вкладку "Конструктор"')
    def click_on_the_constructor(self):
        super().find_and_click_element(MainPageLocators.CONSTRUCTOR_NONE_ACTIVE)

    @allure.step('Получаем активную вкладку "Конструктор"')
    def get_active_constructor(self):
        active_constructor = self.wait_and_find_element(MainPageLocators.CONSTRUCTOR_ACTIVE)
        return active_constructor

    @allure.step('Клик на вкладку "Лента заказов"')
    def click_on_the_order_feed(self):
        super().find_and_click_element(MainPageLocators.ORDER_FEED_NONE_ACTIVE)

    @allure.step('Клик на вкладку "Лента заказов" после регистрации')
    def click_on_the_order_feed_after_auth(self):
        order_feed_button = self.wait_and_find_element(MainPageLocators.ORDER_FEED_NONE_ACTIVE)
        order_feed_button.click()

    @allure.step('Получаем активную вкладку "Лента заказов"')
    def get_active_order_feed(self):
        active_order_feed = self.wait_and_find_element(MainPageLocators.ORDER_FEED_ACTIVE)
        return active_order_feed

    @allure.step('Клик на первый ингредиент')
    def click_to_ingredient(self):
        super().find_and_click_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step('Получаем попап с деталями')
    def get_popup(self):
        popup = self.wait_and_find_element(MainPageLocators.POPUP_INGREDIENT)
        return popup

    @allure.step('Клик на крестик/закрыть попап')
    def click_on_the_cross(self):
        super().find_and_click_element(MainPageLocators.CLOSE_POPUP)

    @allure.step('Получаем первый ингредиент')
    def get_first_ingredient(self):
        first_ingredient = self.wait_and_find_element(MainPageLocators.FIRST_INGREDIENT)
        return first_ingredient

    @allure.step('Добавление булки в заказ')
    def move_bun(self):
        super().move_element(MainPageLocators.FIRST_INGREDIENT, MainPageLocators.TARGET)

    @allure.step('Получаем каунтер в инргредиенте')
    def get_counter(self):
        counter = self.wait_and_find_element(MainPageLocators.COUNTER_HAS_INCREASED)
        return counter

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_on_order_button(self):
        super().find_and_click_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Получаем попап с успешным заказом')
    def get_success_popup(self):
        order_popup = self.wait_and_find_element(MainPageLocators.POPUP_ORDER)
        return order_popup

    @allure.step('Получаем попап с успешным номером заказа')
    def get_success_order(self):
        self.wait_text_element_changed(MainPageLocators.ORDER_INTO_POPUP, '9999')
        order = self.wait_and_find_element(MainPageLocators.ORDER_INTO_POPUP).text
        return order











