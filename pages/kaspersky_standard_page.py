import allure

from pages.kaspersky_base_page import BasePage



class StandardPage(BasePage):

    locators = StandardPageLocators()

    class StandardPageBuyBlock:
        @allure.step('Find Kaspersky Standard price for 1 device 1 year on Main Standard page')
        def check_standard_1d1y_price(self):
        pass