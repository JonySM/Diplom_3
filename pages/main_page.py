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


