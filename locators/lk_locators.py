from selenium.webdriver.common.by import By


class LkPageLocators:
    L_K_BUTTON = (By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")  # Переход в ЛК
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, ".//a[starts-with(@href, '/forgot-password')]")  # Кнопка восстановить пароль
    ACTIVE_PASSWORD_FIELD = (By.XPATH, ".//input[@type='text' and contains(@name, 'Пароль')]")  # Активное поле пароль
    SHOW_SKIP_PASSWORD = (By.XPATH, ".//div[@class='input__icon input__icon-action']")  # Глаз показать/скрыть пароль
    PASSWORD_INPUT_FIELD = (By.XPATH, ".//input[@name='Пароль']")  # Поле ввод пароля
    LOGIN_INPUT_FIELD = (By.XPATH, ".//input[@name='name']")  # Ввод логина(почта)
    LOGIN_MAIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка войти со страницы в ЛК
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка войти в аккаунт
    ACTIVE_HISTORY_ORDER = (By.XPATH, ".//a[@class = 'Account_link__2ETsJ text text_type_main-medium text_color_inactive"
                                      " Account_link_active__2opc9' and (text()='История заказов')]")
                                                                                      # Активная вкладка история заказов
    NONE_ACTIVE_HISTORY_ORDER = \
        (By.XPATH, ".//a[@class = 'Account_link__2ETsJ text text_type_main-medium text_color_inactive' "
                   "and (text()='История заказов')]")  # Неактивная вкладка история заказов
    LOGOUT_BUTTON_INSIDE_LK = (By.XPATH, ".//button[text()='Выход']")  # Кнопка выхода из ЛК
    HISTORY_ORDER = (By.XPATH, "(.//p[@class='text text_type_digits-default'][contains(text(), '{}')])")  # История заказов, определенный заказ









