import helper


class Url:
    STELLAR_BURGERS_URL = "https://stellarburgers.nomoreparties.site"
    BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
    CREATE_USER = 'auth/register'
    DELETE_USER = 'auth/user'


class Data:
    CREATE_RANDOM_USER_BODY = {
        "email": helper.Help.generated_email(),
        "password": 'UserPrakticum!*1234',
        "name": helper.Help.generated_name()
    }

