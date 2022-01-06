from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def go_to_basket(self):
        login_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        login_link.click()

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_ROWS), \
            'Items found in basket while expected not to be'

    def should_be_message_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            'Basket empty message is missing while it was expected'
