from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class OrderFeedPageLocators(BasePage):
    ORDER_IN_WORK = (By.XPATH, "(.//li[@class='text text_type_digits-default mb-2'])[6]")  # Элемент в работе
    POPUP_WITH_DETAILS = (By.XPATH, ".//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']"
                                    "//h2[text()='Флюоресцентный бургер']")  # Попап с деталями
    FIRST_ORDER_IN_FEED = (By.XPATH, ("(.//a[@class='OrderHistory_link__1iNby'])[1]"))  # Первый заказ
    ORDER_IN_FEED = (By.XPATH, "(.//p[@class='text text_type_digits-default'][contains(text(), '{}')])")
    # Заказ пользователя в ленте
    COUNTER_ALL_TIME = (By.XPATH, "(.//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]")
    # Каунтер за все время
    COUNTER_TODAY = (By.XPATH, "(.//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")
    # Каунтер за сегодня
