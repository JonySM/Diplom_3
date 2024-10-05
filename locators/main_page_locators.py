from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_NONE_ACTIVE = \
        (By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")
    #  Неактивная вкладка "конструктор"
    CONSTRUCTOR_ACTIVE = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo']"
                                    "/p[text()='Конструктор']")  # Активная вкладка "Конструктор"
    ORDER_FEED_NONE_ACTIVE = (By.XPATH,
                              ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Лента Заказов']")
    # Неактивная вкладка "Лента Заказов"
    ORDER_FEED_ACTIVE = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo']"
                                   "/p[text()='Лента Заказов']")  # Активна вкладка "Лента Заказов"
    POPUP_INGREDIENT = (By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    # Попап "Детали ингредиентов"
    CLOSE_POPUP = (By.XPATH, ("(.//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK'])[1]"))
    # Крестик
    FIRST_INGREDIENT = (By.XPATH, ("(.//img[@class='BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4'])[1]"))
    # Первый ингредиент
    COUNTER_HAS_INCREASED = (By.XPATH, ".//div[@class='counter_counter__ZNLkj counter_default__28sqi']//p[text()='2']")
    TARGET = (By.XPATH, ("(.//span[@class='constructor-element__row'])[1]"))  # Цель куда перетаскиваем булочку
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__"
                                     "1O7Bx button_button_size_large__G21Vg']")  # Кнопка "Оформить заказ"
    POPUP_ORDER = (By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']")  # Попап заказа
    ORDER_INTO_POPUP = (By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m"
                                  " text text_type_digits-large mb-8']")  # Номер заказа в попап
