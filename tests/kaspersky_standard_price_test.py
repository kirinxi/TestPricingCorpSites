import allure

from data.url import KL_Urls_Global as url
from pages.kaspersky_standard_page import StandardPageBuyBlock
from data.testing_pricelist_data import StandardPriceList

@allure.suite('Kaspersky Standard Prices')
class TestKasperskyStandardPage:

    @allure.feature('Kaspersky Standard Buy Block Prices')
    class TestKasperskyStandardBuyBlock:

        @allure.title('Check Kaspersky Standard Buy Block Prices for 1 device 1 year')
        def test_kaspersky_standard_buy_block_1d1y(self, driver):

            kaspersky_standard_price = kaspersky_standard_buy_block_1d1y.find_kaspersky_standard_buy_block_1d1y_with_discount()
            initindard_buy_block_1d1y = StandardPageBuyBlock(driver, url.STANDARD_SECURITY)
            kaspersky_standard_buy_block_1d1y.open()
            discountal_price = kaspersky_standard_buy_block_1d1y.find_kaspersky_standard_buy_block_1d1y_without_discount()
            renewal_disclaimer_price = \
                kaspersky_standard_buy_block_1d1y.find_kaspersky_standard_buy_block_1d1y_renewal_disclaimer()
            print(discount_price)
            print(initial_price)
            print(renewal_disclaimer_price)

            assert discount_price == StandardPriceList.standard_1d1y, 'Price is not correct in standard_1d1y_buyblock'
            assert initial_price[23:29] == StandardPriceList.standard_1d1y_renewal
            assert renewal_disclaimer_price == StandardPriceList.standard_1d1y_renewal

        @allure.title('Check Kaspersky Standard Buy Block Prices for 3 device 1 year')
        def test_kaspersky_standard_buy_block_3d1y(self, driver):
            kaspersky_standard_buy_block_3d1y = StandardPageBuyBlock(driver, url.STANDARD_SECURITY)
            kaspersky_standard_buy_block_3d1y.open()
            discount_price = kaspersky_standard_buy_block_3d1y.find_kaspersky_standard_buy_block_1d1y_with_discount()
            initial_price = kaspersky_standard_buy_block_3d1y.find_kaspersky_standard_buy_block_1d1y_without_discount()
            renewal_disclaimer_price = \
                kaspersky_standard_buy_block_3d1y.find_kaspersky_standard_buy_block_1d1y_renewal_disclaimer()
            data = kaspersky_standard_buy_block_3d1y.find_kaspersky_standard_buy_block_3d1y_with_discount
            print(discount_price)
            print(initial_price[23:29])
            print(renewal_disclaimer_price)
            print(data)

            assert discount_price == StandardPriceList.standard_3d1y
            assert initial_price[23:29] == StandardPriceList.standard_3d1y_renewal
            assert renewal_disclaimer_price == StandardPriceList.standard_3d1y_renewal

