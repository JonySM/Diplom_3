import allure
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Клик на первый заказ в "Ленте заказов"')
    def click_on_the_first_order_in_feed(self):
        super().find_and_click_element(OrderFeedPageLocators.FIRST_ORDER_IN_FEED)

    @allure.step('Получаем попап заказа')
    def get_popup_order(self):
        popup_order = self.wait_and_find_element(OrderFeedPageLocators.POPUP_WITH_DETAILS)
        return popup_order

    @allure.step('Получаем историю заказа в "Ленте заказов"')
    def get_history_order(self, order_id):
        metod, locator = OrderFeedPageLocators.ORDER_IN_FEED
        return self.is_element_exist((metod, locator.format(order_id)))

    @allure.step('Получаем количество заказов за все время')
    def get_counter_by_all_time(self):
        order = self.wait_and_find_element(OrderFeedPageLocators.COUNTER_ALL_TIME).text
        return order

    @allure.step('Получаем количество заказов за сегодня')
    def get_counter_by_today(self):
        order = self.wait_and_find_element(OrderFeedPageLocators.COUNTER_TODAY).text
        return order

    @allure.step('Получаем заказ в работе')
    def get_order_in_work(self):
        order = self.wait_and_find_element(OrderFeedPageLocators.ORDER_IN_WORK).text
        return order
