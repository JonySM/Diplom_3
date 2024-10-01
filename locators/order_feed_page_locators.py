from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class OrderFeedPageLocators(BasePage):
    ORDER_IN_WORK = (By.XPATH, ".//li[@class='text text_type_digits-default mb-2']")
    POPUP_WITH_DETAILS = (By.XPATH, ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']"
                                    "//h2[text()='Флюоресцентный бургер']")  # Попап с деталями
    FIRST_ORDER_IN_FEED = (By.XPATH, ("(.//a[@class='OrderHistory_link__1iNby'])[1]"))  # Первый заказ
    ORDER_IN_FEED = (By.XPATH, ("(.//p[@class='text text_type_digits-default'])[1]"))
    # Заказ пользователя в ленте
