from pages.main_page import MainPage
from settings import Url


class TestMainPage:
    def test_switch_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.STELLAR_BURGERS_URL)
        main_page.click_on_the_order_feed()
        main_page.click_on_the_constructor()
        assert main_page.get_active_constructor().is_displayed()