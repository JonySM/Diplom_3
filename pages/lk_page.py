import allure
from locators.lk_locators import LkPageLocators
from pages.base_page import BasePage


class LkPage(BasePage):
    def click_on_the_lk_button(self):
        super().find_and_click_element(LkPageLocators.L_K_BUTTON)

    def click_on_the_lk_button_after_registration(self):
        lk_button = self.wait_and_find_element(LkPageLocators.L_K_BUTTON)
        lk_button.click()

    def click_on_the_recovery_button(self):
        super().find_and_click_element(LkPageLocators.RECOVERY_PASSWORD_BUTTON)

    def set_email_for_login(self, email):
        email_login_fild = self.wait_and_find_element(LkPageLocators.LOGIN_INPUT_FIELD)
        email_login_fild.send_keys(email)

    def set_password_for_login(self, password):
        email_login_fild = self.wait_and_find_element(LkPageLocators.PASSWORD_INPUT_FIELD)
        email_login_fild.send_keys(password)

    def click_show_or_skip_eye(self):
        super().find_and_click_element(LkPageLocators.SHOW_SKIP_PASSWORD)

    def get_active_field(self):
        active_field = self.wait_and_find_element(LkPageLocators.ACTIVE_EMAIL_FIELD)
        return active_field

    def get_login_button(self):
        login_button = self.wait_and_find_element(LkPageLocators.LOGIN_MAIN_BUTTON)
        return login_button

    def click_on_the_login_button(self):
        super().find_and_click_element(LkPageLocators.LOGIN_ACCOUNT_BUTTON)

    def set_email_login(self, email):
        email_field = self.wait_and_find_element(LkPageLocators.LOGIN_INPUT_FIELD)
        email_field.send_keys(email)

    def set_password_login(self, password):
        password_field = self.wait_and_find_element(LkPageLocators.PASSWORD_INPUT_FIELD)
        password_field.send_keys(password)

    def click_on_the_login_main_button(self):
        super().find_and_click_element(LkPageLocators.LOGIN_MAIN_BUTTON)

    def click_on_the_history_order_button(self):
        super().find_and_click_element(LkPageLocators.NONE_ACTIVE_HISTORY_ORDER)

    def get_on_active_history_button(self):
        history_button = self.wait_and_find_element(LkPageLocators.ACTIVE_HISTORY_ORDER)
        return history_button

    def click_on_the_logout_button(self):
        logout_button = self.wait_and_find_element(LkPageLocators.LOGOUT_BUTTON_INSIDE_LK)
        logout_button.click()











