from pages.lk_page import LkPage
from settings import Url, Data


class TestLk:
    def test_switch_to_lk(self, driver):
        lk_page = LkPage(driver)
        lk_page.open_page(Url.STELLAR_BURGERS_URL)
        lk_page.click_on_the_lk_button()
        assert lk_page.get_login_button().is_displayed()

    def test_switch_to_history_orders(self, driver, authorization):
        lk_page = LkPage(driver)
        lk_page.click_on_the_lk_button_after_registration()
        lk_page.click_on_the_history_order_button()
        assert lk_page.get_on_active_history_button().is_displayed()

    def test_logout(self, driver, authorization):
        lk_page = LkPage(driver)
        lk_page.click_on_the_lk_button_after_registration()
        lk_page.click_on_the_logout_button()
        assert lk_page.get_login_button().is_displayed()

