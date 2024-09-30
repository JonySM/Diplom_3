from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    RECOVERY_BUTTON = (By.XPATH,
                       ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")  # Кнопка "Восстановить"

    EMAIL_RECOVERY_FILD = (By.XPATH, ".//input[@name='name']")  # Поле ввода email

    CODE_FROM_LETTER_FILD = (By.XPATH, ".//label[text()='Введите код из письма']")  # Поле для ввода кода из письма