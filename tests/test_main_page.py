import allure
from pages.main_page import MainPage
from settings import Url


class TestMainPage:
    @allure.title('Переход по клику на «Конструктор»')
    def test_switch_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.STELLAR_BURGERS_URL)
        main_page.click_on_the_order_feed()
        main_page.click_on_the_constructor()
        assert main_page.get_active_constructor().is_displayed()

    @allure.title('Переход по клику на «Лента заказов»')
    def test_switch_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.STELLAR_BURGERS_URL)
        main_page.click_on_the_order_feed()
        assert main_page.get_active_order_feed().is_displayed()

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_open_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.STELLAR_BURGERS_URL)
        main_page.click_to_ingredient()
        assert main_page.get_popup().is_displayed()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_popup(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.STELLAR_BURGERS_URL)
        main_page.click_to_ingredient()
        main_page.click_on_the_cross()
        assert main_page.get_first_ingredient().is_displayed()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_move_bun(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Url.STELLAR_BURGERS_URL)
        main_page.move_bun()
        assert main_page.get_counter().is_displayed()

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_create_order(self, driver, authorization):
        main_page = MainPage(driver)
        main_page.move_bun()
        main_page.click_on_order_button()
        assert main_page.get_success_popup().is_displayed()


