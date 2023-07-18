from selenium.webdriver.common.by import By


class MainPageLocators:
    SEE_ALL_PRODUCTS = By.XPATH, '//div[contains(@class, "Buttons_buttons")]/a[@href]'
    # Кнопка "See All Products" для перехода на HomeSecurityPage
    COOKIES_BUTTON = By.XPATH, '//button[contains(@class, "CookieBanner")]'
    SCROLLED_H2_ELEMENT = By.ID, "Why choose Kaspersky?"
    STANDARD_PRICE = By.XPATH, '(//div[contains(@class, "OpenBuyBlockColumn_columnContentWrapper")])[1] \
        /descendant::div[contains(@class, "OpenBuyBlockColumn_formPrice")]/descendant::span[2]'
    # Цена на Main-странице за Kaspersky Standard Global
    PLUS_PRICE = By.XPATH, '(//div[contains(@class, "OpenBuyBlockColumn_columnContentWrapper")])[2] \
        /descendant::div[contains(@class, "OpenBuyBlockColumn_formPrice")]/descendant::span[2]'
    # Цена на Main-странице за Kaspersky Plus Global
    PREMIUM_PRICE = By.XPATH, \
        '(//div[contains(@class, "OpenBuyBlockColumn_columnContentWrapper")])[3] \
        /descendant::div[contains(@class, "OpenBuyBlockColumn_formPrice")]/descendant::span[2]'
    # Цена на Main-странице за Kaspersky Premium Global
    STANDARD_LEARN_MORE_BUTTON = By.XPATH, '//a[contains(@class, "Common_linkButton") and @href="/standard"]'
    # Кнопка Learn More на Main-странице за Kaspersky Standard Global
    PLUS_LEARN_MORE_BUTTON = By.XPATH, \
        '//a[contains(@class, "Common_linkButton") and @href="/plus"]'
    # Кнопка Learn More на Main-странице за Kaspersky Plus Global
    PREMIUM_LEARN_MORE_BUTTON = By.XPATH, \
        '//a[contains(@class, "Common_linkButton") and @href="/premium"]'
    # Кнопка Learn More на Main-странице за Kaspersky Premium Global

    MODAL_WINDOW = By.XPATH, '(//div[contains(@class, "Modal_container")])'
    # Модальное окно выбора регионального сайта
    MODAL_WINDOW_BUTTON_KEEP = By.XPATH, '(//span[contains(@text()="Keep browsing on this site")])'


class StandardMainPageLocators:
    MODAL_CONTENT_POPUP = By.CSS_SELECTOR, ('div[data-at-selector="modal-content"]')
    MODAL_CONTENT_CLOSE_BUTTON = By.CSS_SELECTOR, ('div[class*="Modal"]button[type="button"]')
    KASPERSKY_STANDARD_TITLE = By.CSS_SELECTOR, ('div[class*="Product_title"]span[text()="Standard "]')




