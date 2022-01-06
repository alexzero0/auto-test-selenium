import time
import string
import random

import pytest

from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

        page = LoginPage(browser, browser.current_url)
        page.register_new_user(
            str(time.time()) + "@fakemail.org",
            ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)) 
        )

        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser): 
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()

        book_title = page.get_book_title()
        book_price = page.get_book_price()

        page.should_be_added_message(book_title)
        page.should_basket_total_be_same_as_book_price(book_price)

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()

        page.should_not_be_message()

#@pytest.mark.parametrize(
#    'links', 
#    [
#        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
#    ]
#)
def test_guest_can_add_product_to_basket(browser):
    print("SSILKA", link)
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    #book_title = page.get_book_title()
    #book_price = page.get_book_price()

    #page.should_be_added_message(book_title)
    #page.should_basket_total_be_same_as_book_price(book_price)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()

    page.should_not_be_product_in_basket()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()

    page.should_not_be_product_in_basket()
    page.should_be_message_empty()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()

    page.should_not_be_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    page.should_not_be_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

    page.should_message_disappear()
