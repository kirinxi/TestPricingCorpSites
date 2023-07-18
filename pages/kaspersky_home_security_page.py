import time

import allure

from pages.kaspersky_base_page import BasePage
from locators.kaspersky_home_security_page_locators import HomeSecurityPageTopTablePrices as Locators
from locators.kaspersky_base_page_locators import StandardMainPageLocators as Locators2
from locators.kaspersky_base_page_locators import CookieContent as Cookies
from selenium.common.exceptions import UnexpectedAlertPresentException

class HomeSecurityPage(BasePage):

    @allure.step('Accept keep browsing on current region site modal window')
    def accept_keep_browsing_modal_content(self):
        element = self.element_is_visible(Locators.STANDARD_LEARN_MORE_BUTTON)
        self.go_to_element(element)
        self.element_is_visible(Locators2.MODAL_CONTENT_KEEP_BUTTON).click()

    @allure.step('Find Kaspersky Standard price for 1 device 1 year on Home page')
    def get_standard_price_on_home_page(self):
        element = self.element_is_visible(Locators.STANDARD_LEARN_MORE_BUTTON)
        self.go_to_element(element)
        standard_home_page_price = self.element_is_visible(Locators.STANDARD_PRICE).text
        return standard_home_page_price

    @allure.step('Find Kaspersky Plus price for 1 device 1 year on Home page')
    def get_plus_price_on_home_page(self):
        element = self.element_is_visible(Locators.PLUS_LEARN_MORE_BUTTON)
        self.go_to_element(element)
        plus_home_page_price = self.element_is_visible(Locators.PLUS_PRICE).text
        return plus_home_page_price

    @allure.step('Find Kaspersky Premium price for 1 device 1 year on Home page')
    def get_premium_price_on_home_page(self):
        element = self.element_is_visible(Locators.PREMIUM_LEARN_MORE_BUTTON)
        self.go_to_element(element)
        premium_home_page_price = self.element_is_visible(Locators.PREMIUM_PRICE).text
        return premium_home_page_price


