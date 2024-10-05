import allure
from locators.lk_locators import LkPageLocators
from pages.base_page import BasePage


class LkPage(BasePage):
    @allure.step('Клик по кнопке ЛК')
    def click_on_the_lk_button(self):
        super().find_and_click_element(LkPageLocators.L_K_BUTTON)

    @allure.step('Клик по кнопке ЛК после регистрации')  # Данный метод создан, чтобы не падал тест в FF
    def click_on_the_lk_button_after_registration(self):
        lk_button = self.wait_and_find_element(LkPageLocators.L_K_BUTTON)
        lk_button.click()

    @allure.step('Клик по кнопке "Восстановить" в подменю "Забыли пароль?"')
    def click_on_the_recovery_button(self):
        super().find_and_click_element(LkPageLocators.RECOVERY_PASSWORD_BUTTON)

    @allure.step('Заполнить поле email')
    def set_email_for_login(self, email):
        email_login_fild = self.wait_and_find_element(LkPageLocators.LOGIN_INPUT_FIELD)
        email_login_fild.send_keys(email)

    @allure.step('Заполнить поле пароль')
    def set_password_for_login(self, password):
        email_login_fild = self.wait_and_find_element(LkPageLocators.PASSWORD_INPUT_FIELD)
        email_login_fild.send_keys(password)

    @allure.step('Клик на кнопку "глаз"/для видимости пароля')
    def click_show_or_skip_eye(self):
        super().find_and_click_element(LkPageLocators.SHOW_SKIP_PASSWORD)

    @allure.step('Получить активное поле пароль')
    def get_active_field(self):
        active_field = self.wait_and_find_element(LkPageLocators.ACTIVE_PASSWORD_FIELD)
        return active_field

    @allure.step('Получить кнопку войти со страницы ЛК')
    def get_login_button(self):
        login_button = self.wait_and_find_element(LkPageLocators.LOGIN_MAIN_BUTTON)
        return login_button

    @allure.step('Клик на кнопку войти')
    def click_on_the_login_button(self):
        super().find_and_click_element(LkPageLocators.LOGIN_ACCOUNT_BUTTON)

    @allure.step('Заполнить поле email')
    def set_email_login(self, email):
        email_field = self.wait_and_find_element(LkPageLocators.LOGIN_INPUT_FIELD)
        email_field.send_keys(email)

    @allure.step('Заполнить поле пароль')
    def set_password_login(self, password):
        password_field = self.wait_and_find_element(LkPageLocators.PASSWORD_INPUT_FIELD)
        password_field.send_keys(password)

    @allure.step('Заполнить поле пароль')
    def click_on_the_login_main_button(self):
        super().find_and_click_element(LkPageLocators.LOGIN_MAIN_BUTTON)

    @allure.step('Клик на неактивную вкладку "История заказов"')
    def click_on_the_history_order_button(self):
        super().find_and_click_element(LkPageLocators.NONE_ACTIVE_HISTORY_ORDER)

    @allure.step('Возвращает активную вкладку "История заказов"')
    def get_on_active_history_button(self):
        history_button = self.wait_and_find_element(LkPageLocators.ACTIVE_HISTORY_ORDER)
        return history_button

    @allure.step('Клик на кнопку выход')
    def click_on_the_logout_button(self):
        logout_button = self.wait_and_find_element(LkPageLocators.LOGOUT_BUTTON_INSIDE_LK)
        logout_button.click()

    @allure.step('Возвращает заказ внутри лк')
    def get_history_order_into_lk(self, order_id):
        metod, locator = LkPageLocators.HISTORY_ORDER
        return self.is_element_exist((metod, locator.format(order_id)))
