from selenium.webdriver.common.by import By


class HomeSecurityPageLocators:
    HOME_SECURITY_PAGE_INIT = By.XPATH, \
        '//span[contains(text(), "Home Products")]'

class HomeSecurityPageTopTablePrices:
    STANDARD_PRICE = By.XPATH, \
        '(//div[contains(@class, "OpenBuyBlockColumn_columnContentWrapper")])[1] \
        /descendant::div[contains(@class, "OpenBuyBlockColumn_formPrice")]/descendant::span[2]'
    # Цена на Home-странице за Kaspersky Standard Global
    PLUS_PRICE = By.XPATH, \
        '(//div[contains(@class, "OpenBuyBlockColumn_columnContentWrapper")])[2] \
        /descendant::div[contains(@class,"OpenBuyBlockColumn_formPrice")]/descendant::span[2]'
    # Цена на Home-странице за Kaspersky Plus Global
    PREMIUM_PRICE = By.XPATH, \
        '(//div[contains(@class, "OpenBuyBlockColumn_columnContentWrapper")])[3] \
        /descendant::div[contains(@class,"OpenBuyBlockColumn_formPrice")]/descendant::span[2]'
    # Цена на Home-странице за Kaspersky Premium Global
    STANDARD_LEARN_MORE_BUTTON = By.XPATH, \
        '//span[contains (@class, "GreenButton")]/parent::a[contains(@aria-label, "Kaspersky Standard")]'
    # Кнопка Learn More на Home-странице за Kaspersky Standard Global
    PLUS_LEARN_MORE_BUTTON = By.XPATH, \
        '//span[contains (@class, "GreenButton")]/parent::a[contains(@aria-label, "Kaspersky Plus")]'
    # Кнопка Learn More на Home-странице за Kaspersky Plus Global
    PREMIUM_LEARN_MORE_BUTTON = By.XPATH, \
        '//span[contains (@class, "GreenButton")]/parent::a[contains(@aria-label, "Kaspersky Premium")]'
    # Кнопка Learn More на Home-странице за Kaspersky Premium Global

class HomeSecurityPageStandardDropdownList:
    STANDARD_DROPDOWNLIST_1_POSITION = By.XPATH, \
        '(//div[contains(@data-at-bb-title,"Kaspersky Standard")]//span[contains(@class, "PlanSelect_price")])[1]'
    # Цена на 1-ую позинию (1 девайс/1 год) Kaspersky Standard в выпадающем списке пре-выбранных позиций
    STANDARD_DROPDOWNLIST_2_POSITION = By.XPATH, \
        '(//div[contains(@data-at-bb-title,"Kaspersky Standard")]//span[contains(@class, "PlanSelect_price")])[2]'
    # Цена на 2-ую позинию (3 девайса/1 год) Kaspersky Standard в выпадающем списке пре-выбранных позиций

class HomeSecurityPagePlusDropdownList:
    PLUS_DROPDOWNLIST_1_POSITION = By.XPATH, \
        '(//div[contains(@data-at-bb-title,"Kaspersky Plus")]//span[contains(@class, "PlanSelect_price")])[1]'
    # Цена на 1-ую позинию (1 девайс/1 год) Kaspersky Plus в выпадающем списке пре-выбранных позиций
    PLUS_DROPDOWNLIST_2_POSITION = By.XPATH, \
        '(//div[contains(@data-at-bb-title,"Kaspersky Plus")]//span[contains(@class, "PlanSelect_price")])[2]'
    # Цена на 2-ую позинию (3 девайса/1 год) Kaspersky Plus в выпадающем списке пре-выбранных позиций

class HomeSecurityPagePremiumDropdownList:
    PREMIUM_DROPDOWNLIST_1_POSITION = By.XPATH, \
        '(//div[contains(@data-at-bb-title,"Kaspersky Premium")]//span[contains(@class, "PlanSelect_price")])[1]'
    # Цена на 1-ую позинию (1 девайс/1 год) Kaspersky Premium в выпадающем списке пре-выбранных позиций
    PREMIUM_DROPDOWNLIST_2_POSITION = By.XPATH, \
        '(//div[contains(@data-at-bb-title,"Kaspersky Premium")]//span[contains(@class, "PlanSelect_price")])[2]'
    # Цена на 2-ую позинию (3 девайс/1 год) Kaspersky Premium в выпадающем списке пре-выбранных позиций

class HomeSecurityPagePrechosenPositions:
    STANDARD_PRECHOICE = By.XPATH, \
        '//div[contains(@data-at-bb-title,"Kaspersky Standard")]//div[contains(@class, "Price_price")]/span[@data-hidden]'
    # Цена со скидкой пре-выбранного продукта Kaspersky Standard
    PLUS_PRECHOICE = By.XPATH, \
        '//div[contains(@data-at-bb-title,"Kaspersky Plus")]//div[contains(@class, "Price_price")]/span[@data-hidden]'
    # Цена со скидкой пре-выбранного продукта Kaspersky Plus
    PREMIUM_PRECHOICE = By.XPATH, \
        '//div[contains(@data-at-bb-title,"Kaspersky Premium")]//div[contains(@class, "Price_price")]/span[@data-hidden]'
    # Цена со скидкой пре-выбранного продукта Kaspersky Premium

class HomeSecurityPageBottomTableButtons:
    STANDARD_BUYNOW_BUTTON = By.XPATH, \
        '//div[contains(@data-at-bb-title,"Kaspersky Standard")]//button[contains(@class, "Common_button")]'
    STANDARD_LEARNMORE_BOTTOM_BUTTON = By.XPATH, \
        '//div[contains(@data-at-bb-title,"Kaspersky Standard")]//a[contains(@class, "Common_linkButton")]'
    # Кнопки "Купить" и "Узнать ещё" для Kaspersky Standard с выпадающим списком
    PLUS_BUYNOW_BUTTON = By.XPATH, \
        '//div[contains(@data-at-bb-title,"Kaspersky Plus")]//button[contains(@class, "Common_button")]'
    PLUS_LEARNMORE_BOTTOM_BUTTON = By.XPATH, \
        '//div[contains(@data-at-bb-title,"Kaspersky Plus")]//a[contains(@class, "Common_linkButton")]'
    # Кнопки "Купить" и "Узнать ещё" для Kaspersky Plus с выпадающим списком
    PREMIUM_BUYNOE_BUTTON = By.XPATH, \
        '//div[contains(@data-at-bb-title,"Kaspersky Premium")]//button[contains(@class, "Common_button")]'
    PREMIUM_LEARNMORE_BOTTOM_BUTTON = By.XPATH, \
        '//div[contains(@data-at-bb-title,"Kaspersky Premium")]//a[contains(@class, "Common_linkButton")]'
    # Кнопки "Купить" и "Узнать ещё" для Kaspersky Premium с выпадающим списком