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
