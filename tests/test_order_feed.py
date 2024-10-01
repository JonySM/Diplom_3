from pages.lk_page import LkPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from stellar_burger_api import StellarBurgersApi


class TestOrderFeed:
    def test_success_popup(self, driver, create_order):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_on_the_first_order_in_feed()
        assert order_feed_page.get_popup_order().is_displayed()

    def test_order_from_history_in_order_feed(self, driver, create_order):
        order_feed_page = OrderFeedPage(driver)
        lk_feed_page = LkPage(driver)
        main_page = MainPage(driver)
        lk_feed_page.click_on_the_lk_button_after_registration()
        lk_feed_page.click_on_the_history_order_button()
        id_order_from_lk = lk_feed_page.get_history_order_into_lk().text
        main_page.click_on_the_order_feed()
        id_order = order_feed_page.get_history_order().text
        assert id_order_from_lk == id_order





