from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    VIEW_BASKET_BTN=(By.CSS_SELECTOR, "[href*='/basket/']")

#class MainPageLocators():

class LoginPageLocators():
    LOGIN_FORM=(By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM=(By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BTN=(By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME=(By.CSS_SELECTOR,".product_main > h1")
    PRODUCT_PRICE=(By.CSS_SELECTOR,".product_main > .price_color")

    PRODUCT_NAME_IN_BASKET=(By.CSS_SELECTOR, "#messages > div.alert:nth-child(1)  .alertinner  strong")
    PRODUCT_PRICE_IN_BASKET=(By.CSS_SELECTOR,"#messages  .alert-info  .alertinner  strong")

class BasketPageLocators():
    BASKET_IS_EMPTY_TEXT=(By.CSS_SELECTOR,"#content_inner > p")
    PRODUCT_IN_BASKET=(By.CSS_SELECTOR, ".basket-items .row")

