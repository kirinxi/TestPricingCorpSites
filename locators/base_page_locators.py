from selenium.webdriver.common.by import By

class CookieContent:
    COOKIES_BANNER = By.CSS_SELECTOR, ('section[data-at-selector="cookie-banner"]')
    ACCEPT_COOKIES_BUTTON = By.CSS_SELECTOR, ('button[data-at-selector="cookie-banner-btn"]')

class StandardMainPageLocators:
    MODAL_CONTENT_POPUP = (By.CSS_SELECTOR, 'div[data-at-selector="modal-content"]')
    MODAL_CONTENT_KEEP_BUTTON = By.XPATH, \
        '//div[contains(@class, "LocalPopup_footer")]/button[contains(@class, "Button")]'
    MODAL_CONTENT_CLOSE_BUTTON = (By.CSS_SELECTOR, 'div[class*="Modal"]button[type="button"]')

    KASPERSKY_STANDARD_TITLE = (By.CSS_SELECTOR, 'div[class*="Product_title"]span[text()="Standard "]')