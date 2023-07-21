import time

import allure
from selenium.common import TimeoutException

from locators.kaspersky_standard_page_locators import StandardPageBuyBlockLocators, \
    StandardPageDialogWindows
from pages.kaspersky_base_page import BasePage


class StandardPageBuyBlock(BasePage):
    locators = StandardPageBuyBlockLocators()
    locators2 = StandardPageDialogWindows()

    #1 DEVICE - 1 YEAR
    @allure.step('Find price for Kaspersky Standard on Buy Block for 1 device 1 year with discount')
    def find_kaspersky_standard_buy_block_1d1y_with_discount(self):
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_SELECTION).click()
        self.element_is_clickable(self.locators.STANDARD_BUY_BLOCK_CONTENT_1D1Y_DROPDOWN_LIST).click()
        modal_window = self.element_is_not_visible(self.locators2.STANDARD_SPECIAL_OFFER_MODAL)
        standard_buy_block_1d1y_discount_price = \
            self.element_is_present(self.locators.STANDARD_BUY_BLOCK_CONTENT_WITH_DISCOUNT).get_attribute("innerHTML")
        try:
            modal_window
        except TimeoutException:
            return standard_buy_block_1d1y_discount_price
        return standard_buy_block_1d1y_discount_price

    @allure.step('Find price for Kaspersky Standard on Buy Block for 1 device 1 year without discount')
    def find_kaspersky_standard_buy_block_1d1y_without_discount(self):
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_SELECTION).click()
        self.element_is_clickable(self. locators.STANDARD_BUY_BLOCK_CONTENT_1D1Y_DROPDOWN_LIST).click()
        standard_buy_block_1d1y_initial_price = \
            self.element_is_present(self.locators.STANDARD_BUY_BLOCK_CONTENT_WITHOUT_DISCOUNT).get_attribute("innerHTML")
        return standard_buy_block_1d1y_initial_price

    @allure.step('Find renewal price for Kaspersky Standard on Buy Block for 1 device 1 year in disclaimer')
    def find_kaspersky_standard_buy_block_1d1y_renewal_disclaimer(self):
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_SELECTION).click()
        self.element_is_clickable(self.locators.STANDARD_BUY_BLOCK_CONTENT_1D1Y_DROPDOWN_LIST).click()
        standard_buy_block_1d1y_renewal_price = \
            self.element_is_visible(self.locators.STANDARD_DISCLAIMER_BUY_BLOCK_RENEWAL_PRICE).text
        return standard_buy_block_1d1y_renewal_price

        # 3 DEVICE - 1 YEAR
    @allure.step('Find price for Kaspersky Standard on Buy Block for 3 device 1 year with discount')
    def find_kaspersky_standard_buy_block_3d1y_with_discount(self):
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_SELECTION).click()
        listbox = self.elements_are_visible(self.locators.STANDARD_BUY_BLOCK_LISTBOX)
        for item in listbox:
            self.action_move_to_element([2])
            self. element_is_visible(item)
            data.append(item.text)
        return data

        #self.element_is_clickable(self.locators.STANDARD_BUY_BLOCK_CONTENT_3D1Y_DROPDOWN_LIST).click()
        #standard_buy_block_3d1y_discount_price = \
        #    self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_CONTENT_WITH_DISCOUNT).get_attribute("innerHTML")
        #return standard_buy_block_3d1y_discount_price

    @allure.step('Find price for Kaspersky Standard on Buy Block for 3 device 1 year without discount')
    def find_kaspersky_standard_buy_block_3d1y_without_discount(self):
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_SELECTION).click()
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_CONTENT_3D1Y_DROPDOWN_LIST).click()
        standard_buy_block_3d1y_initial_price = \
            self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_CONTENT_WITHOUT_DISCOUNT).get_attribute("innerHTML")
        return standard_buy_block_3d1y_initial_price

    @allure.step('Find renewal price for Kaspersky Standard on Buy Block for 3 device 1 year in disclaimer')
    def find_kaspersky_standard_buy_block_3d1y_renewal_disclaimer(self):
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_SELECTION).click()
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_CONTENT_3D1Y_DROPDOWN_LIST).click()
        standard_buy_block_3d1y_renewal_price = \
            self.element_is_visible(self.locators.STANDARD_DISCLAIMER_BUY_BLOCK_RENEWAL_PRICE).text
        return standard_buy_block_3d1y_renewal_price


    # 5 DEVICE - 1 YEAR
    @allure.step('Find price for Kaspersky Standard on Buy Block for 5 device 1 year with discount')
    def find_kaspersky_standard_buy_block_5d1y_with_discount(self):
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_SELECTION).click()
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_CONTENT_5D1Y_DROPDOWN_LIST).click()
        standard_buy_block_5d1y_discount_price = \
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_CONTENT_WITH_DISCOUNT).text
        return standard_buy_block_5d1y_discount_price


    @allure.step('Find price for Kaspersky Standard on Buy Block for 5 device 1 year without discount')
    def find_kaspersky_standard_buy_block_5d1y_without_discount(self):
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_SELECTION).click()
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_CONTENT_5D1Y_DROPDOWN_LIST).click()
        standard_buy_block_5d1y_initial_price = \
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_CONTENT_WITHOUT_DISCOUNT).text
        return standard_buy_block_5d1y_initial_price


    @allure.step('Find renewal price for Kaspersky Standard on Buy Block for 5 device 1 year in disclaimer')
    def find_kaspersky_standard_buy_block_5d1y_renewal_disclaimer(self):
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_SELECTION).click()
        self.element_is_visible(self.locators.STANDARD_BUY_BLOCK_CONTENT_5D1Y_DROPDOWN_LIST).click()
        standard_buy_block_5d1y_renewal_price = \
        self.element_is_visible(self.locators.STANDARD_DISCLAIMER_BUY_BLOCK_RENEWAL_PRICE).text
        return standard_buy_block_5d1y_renewal_price
