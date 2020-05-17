from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME_FROM_ALERT_SUCCESS = (By.XPATH, '//div[text()[contains(.,"has been added to your basket")]]/strong')
    PRICE_BASKET_FROM_ALERT_SUCCESS = (
        By.XPATH, '//p[text()[contains(.,"Your basket total is now")]]/strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
