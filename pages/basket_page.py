from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        if self.browser.current_url == 'data:,':
            self.open()

    def should_be_goods(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE)

    def basket_is_empty(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_no_empty_basket_message(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
