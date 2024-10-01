from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_on_the_constructor(self):
        super().find_and_click_element(MainPageLocators.CONSTRUCTOR_NONE_ACTIVE)

    def get_active_constructor(self):
        active_constructor = self.wait_and_find_element(MainPageLocators.CONSTRUCTOR_ACTIVE)
        return active_constructor

    def click_on_the_order_feed(self):
        super().find_and_click_element(MainPageLocators.ORDER_FEED_NONE_ACTIVE)

    def get_active_order_feed(self):
        active_order_feed = self.wait_and_find_element(MainPageLocators.ORDER_FEED_ACTIVE)
        return active_order_feed

    def click_to_ingredient(self):
        super().find_and_click_element(MainPageLocators.FIRST_INGREDIENT)

    def get_popup(self):
        popup = self.wait_and_find_element(MainPageLocators.POPUP_INGREDIENT)
        return popup

    def click_on_the_cross(self):
        super().find_and_click_element(MainPageLocators.CLOSE_POPUP)

    def get_first_ingredient(self):
        first_ingredient = self.wait_and_find_element(MainPageLocators.FIRST_INGREDIENT)
        return first_ingredient

    def move_bun(self):
        super().move_element(MainPageLocators.FIRST_INGREDIENT, MainPageLocators.TARGET)

    def get_counter(self):
        counter = self.wait_and_find_element(MainPageLocators.COUNTER_HAS_INCREASED)
        return counter

    def click_on_order_button(self):
        super().find_and_click_element(MainPageLocators.CREATE_ORDER_BUTTON)

    def get_success_popup(self):
        order_popup = self.wait_and_find_element(MainPageLocators.POPUP_ORDER)
        return order_popup










