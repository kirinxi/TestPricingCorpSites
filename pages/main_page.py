import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators
from locators.main_page_locators import StandardMainPageLocators as LocatorsStandard


class MainPage(BasePage):

    @allure.step('Find Kaspersky Standard price for 1 device 1 year on Main page')
    def get_standard_price_on_main_page(self):
        main_page_price = self.element_is_visible(Locators.STANDARD_PRICE).text
        return main_page_price

    @allure.step('From Main page Standard block go to Kaspersky standard page')
    def go_to_standard_page(self):
        self.go_to_element(Locators.STANDARD_LEARN_MORE_BUTTON)
        self.element_is_clickable(Locators.STANDARD_LEARN_MORE_BUTTON).click()

    @allure.step('Find Kaspersky Plus price for 1 device 1 year on Main page')
    def get_plus_price_on_main_page(self):
        main_page_price = self.element_is_visible(Locators.PLUS_PRICE).text
        return main_page_price

    @allure.step('From Main page Standard block go to Kaspersky standard page')
    def go_to_plus_page(self):
        self.go_to_element(Locators.PLUS_LEARN_MORE_BUTTON)
        self.element_is_clickable(Locators.PLUS_LEARN_MORE_BUTTON).click()

    @allure.step('Find Kaspersky Premium price for 1 device 1 year on Main page')
    def get_premium_price_on_main_page(self):
        main_page_price = self.element_is_visible(Locators.PREMIUM_PRICE).text
        return main_page_price

    @allure.step('From Main page Premium block go to Kaspersky Premium page')
    def go_to_premium_page(self):
        self.go_to_element(Locators.PREMIUM_LEARN_MORE_BUTTON)
        self.element_is_clickable(Locators.PREMIUM_LEARN_MORE_BUTTON).click()