from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAIL_FIELD = (By.ID, 'id_registration-email')
    PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    PASSWORD_CONFIRM_FIELD = (By.ID, 'id_registration-password2')
    REFISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME_FROM_ALERT_SUCCESS = (By.XPATH, '//div[text()[contains(.,"has been added to your basket")]]/strong')
    PRICE_BASKET_FROM_ALERT_SUCCESS = (
        By.XPATH, '//p[text()[contains(.,"Your basket total is now")]]/strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')


class BasePageLocators:
    USER_ICON = (By.CLASS_NAME, 'icon-user')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    BASKET_EMPTY_MESSAGE = (By.XPATH, '//p[text()[contains(.,"empty")]]')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
