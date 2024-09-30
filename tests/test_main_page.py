from pages.main_page import MainPage
from settings import Url


class TestMainPage:
    def test_switch_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.STELLAR_BURGERS_URL)
        main_page.click_on_the_order_feed()
        main_page.click_on_the_constructor()
        assert main_page.get_active_constructor().is_displayed()

    def test_switch_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.STELLAR_BURGERS_URL)
        main_page.click_on_the_order_feed()
        assert main_page.get_active_order_feed().is_displayed()

    def test_open_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.STELLAR_BURGERS_URL)
        main_page.click_to_ingredient()
        assert main_page.get_popup().is_displayed()

    def test_close_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.STELLAR_BURGERS_URL)
        main_page.click_to_ingredient()
        main_page.click_on_the_cross()
        assert main_page.get_first_ingredient().is_displayed()

    def test_move_bun(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.STELLAR_BURGERS_URL)
        main_page.move_bun()
        assert main_page.get_counter().is_displayed()

    def test_create_order(self, driver, authorization):
        main_page = MainPage(driver)
        main_page.move_bun()
        main_page.click_on_order_button()
        assert main_page.get_success_popup().is_displayed()


