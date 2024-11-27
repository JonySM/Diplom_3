import allure
import requests
from settings import Data, Url


class StellarBurgersApi:
    @staticmethod
    @allure.step('Метод создания случайного пользователя')
    def create_new_random_user():
        body = Data.CREATE_RANDOM_USER_BODY
        return requests.post(Url.BASE_URL + Url.CREATE_USER, json=body, verify=False)

    @staticmethod
    @allure.step('Метод удаления пользователя')
    def delete_user(accesstoken):
        headers = {'Authorization': accesstoken}
        response_delete = requests.delete(f'{Url.BASE_URL + Url.DELETE_USER}', headers=headers, verify=False)
        return response_delete

