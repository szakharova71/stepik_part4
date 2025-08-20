from .pages.product_page import ProductPage
import pytest

offernumberlist=[0,1,2,3,4,5,6,pytest.param(7, marks=pytest.mark.xfail),8,9]

@pytest.mark.parametrize ('offernumber',offernumberlist)
def test_guest_can_add_product_to_basket(browser, offernumber):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offernumber}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.message_is_displayed()
    page.basket_sum_same_as_product()


