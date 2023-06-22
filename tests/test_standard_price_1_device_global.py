import allure

from data.url import KL_Urls_Global as Url
from pages.main_page import MainPage
from pages.home_security_page import HomeSecurityPage


@allure.suite('Test prices between Main and Home pages on Global')
class TestPriceMainAndHomeGlobal:

    @allure.title('Check Kaspersky Standard price for 1 device 1 year on Main and Home pages')
    def test_standard_price_for_1_device_main_home(self, driver):
        price_main = MainPage(driver, Url.MAIN_PAGE_GLOBAL)
        price_main.open()
        main_page_price = price_main.get_standard_price_on_main_page()

        standard_home_page = HomeSecurityPage(driver, Url.HOME_SECURITY)
        standard_home_page.open()
        standard_home_page.accept_keep_browsing_modal_content()
        standard_home_page.get_standard_price_on_home_page()
        standard_home_page_price = standard_home_page.get_standard_price_on_home_page()

        assert main_page_price == standard_home_page_price
        print(main_page_price)

    @allure.title('Check Kaspersky Plus price for 1 device 1 year on Main and Home pages')
    def test_plus_price_for_1_device_main_home(self, driver):
        price_main = MainPage(driver, Url.MAIN_PAGE_GLOBAL)
        price_main.open()
        main_page_price = price_main.get_plus_price_on_main_page()

        plus_home_page = HomeSecurityPage(driver, Url.HOME_SECURITY)
        plus_home_page.open()
        plus_home_page.accept_keep_browsing_modal_content()
        plus_home_page.get_plus_price_on_home_page()
        plus_home_page_price = plus_home_page.get_plus_price_on_home_page()

        assert main_page_price == plus_home_page_price
        print(main_page_price)

    @allure.title('Check Kaspersky Premium price for 1 device 1 year on Main and Home pages')
    def test_premium_price_for_1_device_main_home(self, driver):
        price_main = MainPage(driver, Url.MAIN_PAGE_GLOBAL)
        price_main.open()
        main_page_price = price_main.get_premium_price_on_main_page()

        premium_home_page = HomeSecurityPage(driver, Url.HOME_SECURITY)
        premium_home_page.open()
        premium_home_page.accept_keep_browsing_modal_content()
        premium_home_page.get_premium_price_on_home_page()
        premium_home_page_price = premium_home_page.get_premium_price_on_home_page()

        assert main_page_price == premium_home_page_price
        print(main_page_price)