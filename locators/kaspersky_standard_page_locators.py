from selenium.webdriver.common.by import By


class StandardPageDialogWindows:
    STANDARD_SPECIAL_OFFER_MODAL = By.XPATH, '//div[@data-at-selector="modal-content"]'
    STANDARD_SPECIAL_OFFER_MODAL_CLOSE_BUTTON = By.XPATH, \
        '//div[contains(@class, "Modal")]//button[contains(@class, "AccesibilityButton")]'

class StandardPageBuyBlockLocators:
    STANDARD_BUY_BLOCK_SELECTION = By.XPATH, \
        '(//div[contains(@class, "Value") and @data-at-selector="select-value"])[2]'
    STANDARD_BUY_BLOCK_LISTBOX = By.XPATH, '//div[contains(@class, "CustomScroll")]'
    STANDARD_BUY_BLOCK_CONTENT_1D1Y_DROPDOWN_LIST = By.XPATH, '(//div[contains(@class, "Option")])[1]'
    STANDARD_BUY_BLOCK_CONTENT_3D1Y_DROPDOWN_LIST = By.XPATH, '(//div[contains(@class, "Option")])[2]'
    STANDARD_BUY_BLOCK_CONTENT_5D1Y_DROPDOWN_LIST = By.XPATH, '(//div[contains(@class, "Option")])[3]'
    STANDARD_BUY_BLOCK_CONTENT_1D2Y_DROPDOWN_LIST = By.XPATH, '(//div[contains(@class, "Option")])[4]'
    STANDARD_BUY_BLOCK_CONTENT_3D2Y_DROPDOWN_LIST = By.XPATH, '(//div[contains(@class, "Option")])[5]'
    STANDARD_BUY_BLOCK_CONTENT_5D2Y_DROPDOWN_LIST = By.XPATH, '(//div[contains(@class, "Option")])[6]'
    STANDARD_BUY_BLOCK_CONTENT_WITH_DISCOUNT = By.XPATH, \
        '(//div[@data-at-device-count="1" and @data-at-device-period="1"]//span[@data-hidden])[2]'
    STANDARD_BUY_BLOCK_CONTENT_WITHOUT_DISCOUNT = By.XPATH, '(//div[@data-at-selector="current-price-container" and \
        @data-at-device-count="1" and @data-at-device-period="1"]//span[@data-hidden])[1]'
    STANDARD_DISCLAIMER_BUY_BLOCK_RENEWAL_PRICE = By.XPATH, \
        '(//div[contains(@class, "BuyBlock_disclaimer")]/span[2])[1]'


class OpenBuyBlockLocators:
    STANDARD_DROPDOWN_LIST_SELECTION = By.XPATH, \
        '(//div[@data-at-product-id="standard"]//*[name()="svg"])[3]'
    STANDARD_1D1Y_OPEN_BUY_BLOCK_DROPDOWN_LIST = By.XPATH, '(//div[contains(@class, "Option")])[1]'
    STANDARD_3D1Y_OPEN_BUY_BLOCK_DROPDOWN_LIST = By.XPATH, '(//div[contains(@class, "Option")])[2]'
    STANDARD_5D1Y_OPEN_BUY_BLOCK_DROPDOWN_LIST = By.XPATH, '(//div[contains(@class, "Option")])[3]'
    STANDARD_1D2Y_OPEN_BUY_BLOCK_DROPDOWN_LIST = By.XPATH, '(//div[contains(@class, "Option")])[4]'
    STANDARD_3D2Y_OPEN_BUY_BLOCK_DROPDOWN_LIST = By.XPATH, '(//div[contains(@class, "Option")])[5]'
    STANDARD_5D2Y_OPEN_BUY_BLOCK_DROPDOWN_LIST = By.XPATH, '(//div[contains(@class, "Option")])[6]'
    STANDARD_1D1Y_OPEN_BUY_BLOCK_PRICE_WITH_DISCOUNT = By.XPATH, \
        '(//div[@data-at-selector="buy-block" and @data-at-product-id="standard" and @data-at-device-count="1" and \
        @data-at-device-period="1"]//span[@data-hidden])[2]'
    STANDARD_1D1Y_OPEN_BUY_BLOCK_PRICE_WITHOUT_DISCOUNT = By.XPATH, \
        '(//div[@data-at-selector="buy-block" and @data-at-product-id="standard" and @data-at-device-count="1" and \
        @data-at-device-period="1"]//span[@data-hidden])[1]'
    STANDARD_3D1Y_OPEN_BUY_BLOCK_PRICE_WITH_DISCOUNT = By.XPATH, \
        '(//div[@data-at-selector="buy-block" and @data-at-product-id="standard" and @data-at-device-count="3" and \
        @data-at-device-period="1"]//span[@data-hidden])[2]'
    STANDARD_3D1Y_OPEN_BUY_BLOCK_PRICE_WITHOUT_DISCOUNT = By.XPATH, \
        '(//div[@data-at-selector="buy-block" and @data-at-product-id="standard" and @data-at-device-count="3" and \
        @data-at-device-period="1"]//span[@data-hidden])[1]'
    STANDARD_5D1Y_OPEN_BUY_BLOCK_PRICE_WITH_DISCOUNT = By.XPATH, \
        '(//div[@data-at-selector="buy-block" and @data-at-product-id="standard" and @data-at-device-count="5" and \
        @data-at-device-period="1"]//span[@data-hidden])[2]'
    STANDARD_5D1Y_OPEN_BUY_BLOCK_PRICE_WITHOUT_DISCOUNT = By.XPATH, \
        '(//div[@data-at-selector="buy-block" and @data-at-product-id="standard" and @data-at-device-count="5" and \
        @data-at-device-period="1"]//span[@data-hidden])[1]'
    STANDARD_1D2Y_OPEN_BUY_BLOCK_PRICE_WITH_DISCOUNT = By.XPATH, \
        '(//div[@data-at-selector="buy-block" and @data-at-product-id="standard" and @data-at-device-count="1" and \
        @data-at-device-period="2"]//span[@data-hidden])[2]'
    STANDARD_1D2Y_OPEN_BUY_BLOCK_PRICE_WITHOUT_DISCOUNT = By.XPATH, \
        '(//div[@data-at-selector="buy-block" and @data-at-product-id="standard" and @data-at-device-count="1" and \
        @data-at-device-period="2"]//span[@data-hidden])[1]'
    STANDARD_3D2Y_OPEN_BUY_BLOCK_PRICE_WITH_DISCOUNT = By.XPATH, \
        '(//div[@data-at-selector="buy-block" and @data-at-product-id="standard" and @data-at-device-count="3" and \
        @data-at-device-period="2"]//span[@data-hidden])[2]'
    STANDARD_3D2Y_OPEN_BUY_BLOCK_PRICE_WITHOUT_DISCOUNT = By.XPATH, \
        '(//div[@data-at-selector="buy-block" and @data-at-product-id="standard" and @data-at-device-count="3" and \
        @data-at-device-period="2"]//span[@data-hidden])[1]'
    STANDARD_5D_2Y_OPEN_BUY_BLOCK_PRICE_WITH_DISCOUNT = By.XPATH, \
        '(//div[@data-at-selector="buy-block" and @data-at-product-id="standard" and @data-at-device-count="5" and \
        @data-at-device-period="2"]//span[@data-hidden])[2]'
    STANDARD_5D2Y_OPEN_BUY_BLOCK_PRICE_WITHOUT_DISCOUNT = By.XPATH, \
        '(//div[@data-at-selector="buy-block" and @data-at-product-id="standard" and @data-at-device-count="5" and \
        @data-at-device-period="2"]//span[@data-hidden])[1]'
    STANDARD_DISCLAIMER_OPEN_BUY_BLOCK_RENEWAL_PRICE = By.XPATH, '(//div[contains(@class, "BuyBlock_disclaimer")] \
        /span[2])[2]'