import allure
from pages.forgot_password_page import ForgotPasswordPage
from pages.lk_page import LkPage
from settings import Url, Data


class TestForgotPassword:
    @allure.title('Переход на страницу восстановления пароля')
    def test_switch_to_the_page_forgot_password(self, driver):
        lk_page = LkPage(driver)
        lk_page.open_page(Url.STELLAR_BURGERS_URL)
        lk_page.click_on_the_lk_button()
        lk_page.click_on_the_recovery_button()
        forgot_page = ForgotPasswordPage(driver)
        assert forgot_page.get_success_button().is_displayed()

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_send_email_and_recovery_click(self, create_random_user, driver):
        lk_page = LkPage(driver)
        lk_page.open_page(Url.STELLAR_BURGERS_URL)
        lk_page.click_on_the_lk_button()
        lk_page.click_on_the_recovery_button()
        forgot_page = ForgotPasswordPage(driver)
        user = create_random_user.json()['user']
        email = user['email']
        forgot_page.set_email_for_recovery(email)
        forgot_page.click_on_big_recovery_button()
        assert forgot_page.get_success_code_for_recovery_fild().is_displayed()

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    def test_active_fild(self, create_random_user, driver):
        lk_page = LkPage(driver)
        lk_page.open_page(Url.STELLAR_BURGERS_URL)
        lk_page.click_on_the_lk_button()
        email = create_random_user.json()['user']['email']
        lk_page.set_email_for_login(email)
        lk_page.set_password_for_login(Data.CREATE_RANDOM_USER_BODY.get('password'))
        lk_page.click_show_or_skip_eye()
        assert lk_page.get_active_field().is_displayed()







