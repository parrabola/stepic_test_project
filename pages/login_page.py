from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'login" not in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register form not present'

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_2_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_FIELD)
        button = self.browser.find_element(*LoginPageLocators.REFISTER_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_2_field.send_keys(password)
        button.click()
