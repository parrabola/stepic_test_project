from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        if self.browser.current_url == 'data:,':
            self.open()

        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def costs_must_match(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRICE_BASKET_FROM_ALERT_SUCCESS).text == self.product_price

    def names_must_match(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_FROM_ALERT_SUCCESS).text == self.product_name
