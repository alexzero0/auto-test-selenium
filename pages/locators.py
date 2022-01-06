from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators(BasePageLocators):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")#login_link_invalid ##login_link


class LoginPageLocators(BasePageLocators):
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, '#register_form > button')



class ProductPageLocators(BasePageLocators):
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, "#messages > div.alert-success")
    BASKET_TOTAL = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs')
    BOOK_TITLE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")

class BasketPageLocators(BasePageLocators):
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs > span > a')
    ITEM_ROWS = (By.CSS_SELECTOR, '#basket_formset > div > div')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
