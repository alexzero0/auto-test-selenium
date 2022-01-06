from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_field.send_keys(email)

        password1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD1)
        password1.send_keys(password)

        password2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD2)
        password2.send_keys(password)

        btn = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON)
        btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_keyword_present_in_url('login')

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)
