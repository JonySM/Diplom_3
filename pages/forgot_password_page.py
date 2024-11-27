import allure
from locators.forgot_password_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step('Проверяем наличие кнопки восстановить')
    def get_success_button(self):
        success_recovery_button = self.wait_and_find_element(ForgotPasswordPageLocators.RECOVERY_BUTTON)
        return success_recovery_button

    @allure.step('Заполняем поле email')
    def set_email_for_recovery(self, email):
        email_fild = self.wait_and_find_element(ForgotPasswordPageLocators.EMAIL_RECOVERY_FILD)
        email_fild.send_keys(email)

    @allure.step('Возвращаем поля для ввода кода восстановления из письма')
    def get_success_code_for_recovery_fild(self):
        success_code_fild = self.wait_and_find_element(ForgotPasswordPageLocators.CODE_FROM_LETTER_FILD)
        return success_code_fild

    @allure.step('Клик по основной/по которой получаем код) кнопки "Восстановить"')
    def click_on_big_recovery_button(self):
        super().find_and_click_element(ForgotPasswordPageLocators.RECOVERY_BUTTON)

