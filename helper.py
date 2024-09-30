import random
import allure


class Help:
    @staticmethod
    @allure.step('Создаем случайный email пользователя')
    def generated_email():
        return f"UserPrakticum{random.randint(100, 9999)}@yandex.ru"


    @staticmethod
    @allure.step('Создаем случайное имя пользователя')
    def generated_name():
        return f"Джони{random.randint(100, 999)}"
