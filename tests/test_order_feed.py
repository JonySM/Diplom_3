import allure
from pages.lk_page import LkPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeed:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_success_popup(self, driver, create_order):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_on_the_first_order_in_feed()
        assert order_feed_page.get_popup_order().is_displayed()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_from_history_in_order_feed(self, driver, create_order):
        order_feed_page = OrderFeedPage(driver)
        lk_feed_page = LkPage(driver)
        main_page = MainPage(driver)
        lk_feed_page.click_on_the_lk_button_after_registration()
        lk_feed_page.click_on_the_history_order_button()
        id_order_from_lk = lk_feed_page.get_history_order_into_lk(create_order)
        main_page.click_on_the_order_feed()
        id_order = order_feed_page.get_history_order(create_order)
        assert id_order is True
        assert id_order_from_lk is True

    @allure.title('Cчётчик Выполнено за всё время увеличивается')
    def test_counter_by_all_time(self, driver, authorization):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_on_the_order_feed_after_auth()
        counter_before = order_feed_page.get_counter_by_all_time()
        main_page.click_on_the_constructor()
        main_page.move_bun()
        main_page.click_on_order_button()
        main_page.get_success_order()
        main_page.click_on_the_cross()
        main_page.click_on_the_order_feed()
        counter_after = order_feed_page.get_counter_by_all_time()
        assert counter_after > counter_before

    @allure.title('Cчётчик Выполнено за сегодня')
    def test_counter_by_today(self, driver, authorization):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        main_page.click_on_the_order_feed_after_auth()
        counter_before = order_feed_page.get_counter_by_today()
        main_page.click_on_the_constructor()
        main_page.move_bun()
        main_page.click_on_order_button()
        main_page.get_success_order()
        main_page.click_on_the_cross()
        main_page.click_on_the_order_feed()
        counter_after = order_feed_page.get_counter_by_today()
        assert counter_after > counter_before

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work(self, driver, authorization):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_on_the_order_feed_after_auth()
        main_page.click_on_the_constructor()
        main_page.move_bun()
        main_page.click_on_order_button()
        order_id = main_page.get_success_order()
        main_page.click_on_the_cross()
        main_page.click_on_the_order_feed()
        order_in_work = order_feed_page.get_order_in_work()
        assert f'0{order_id}' == order_in_work










