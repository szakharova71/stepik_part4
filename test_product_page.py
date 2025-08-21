from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest


offernumberlist=[0,1,2,3,4,5,6,pytest.param(7, marks=pytest.mark.xfail),8,9]
#offernumberlist=[0] #for testing

@pytest.mark.parametrize ('offernumber',offernumberlist)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, offernumber):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offernumber}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.message_is_displayed()
    page.basket_sum_same_as_product()

@pytest.mark.xfail
@pytest.mark.parametrize ('offernumber',offernumberlist)
def test_guest_cant_see_success_message_after_adding_product_to_basket  (browser,offernumber):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offernumber}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.parametrize ('offernumber',offernumberlist)
def test_guest_cant_see_success_message(browser, offernumber):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offernumber}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
@pytest.mark.parametrize ('offernumber',offernumberlist)
def test_message_disappeared_after_adding_product_to_basket(browser, offernumber):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offernumber}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.message_is_disappeared()

@pytest.mark.parametrize ('offernumber',offernumberlist)
def test_guest_should_see_login_link_on_product_page(browser, offernumber):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offernumber}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.parametrize ('offernumber',offernumberlist)
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, offernumber):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offernumber}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.parametrize ('offernumber',offernumberlist)
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser,offernumber):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offernumber}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_is_empty()
    basket_page.check_empty_basket_text()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        registerlink="http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        # open register page
        register_page = LoginPage(browser,registerlink)
        register_page.open()
        register_page.should_be_login_page()
        #register user
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        register_page.register_new_user(email, password)
        #check that user logged in
        register_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.message_is_displayed()
        page.basket_sum_same_as_product()
