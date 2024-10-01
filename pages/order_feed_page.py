from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def click_on_the_first_order_in_feed(self):
        super().find_and_click_element(OrderFeedPageLocators.FIRST_ORDER_IN_FEED)

    def get_popup_order(self):
        popup_order = self.wait_and_find_element(OrderFeedPageLocators.POPUP_WITH_DETAILS)
        return popup_order

    def get_history_order(self):
        history_order = self.wait_and_find_element(OrderFeedPageLocators.ORDER_IN_FEED)
        return history_order
