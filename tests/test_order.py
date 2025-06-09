from pages.order_page import OrderPage
from locators.order_page_locators import ORDER_LOCATORS
from conftest import *
from data import order_data
import pytest
import allure

class Test_Order:
    @allure.title("Проверка возможности оформления заказа через кнопку 'Заказать' в заголовке страницы")
    @pytest.mark.parametrize('order_info', order_data.order_info)
    def test_order_samokat(self, driver, order_info):
        order_page = OrderPage(driver)
        order_page.go_to_url()

        order_page.clicl_to_order_button()

        order_page.send_name_in_order_page(order_info['name'])
        order_page.send_soname_in_order_page(order_info['soname'])
        order_page.send_address_in_order_page(order_info['address'])
        order_page.select_metro_station_in_order_page(order_info['metro'])
        order_page.send_phone_in_order_page(order_info['phone'])

        order_page.click_next_in_order_page()

        order_page.select_date_start(order_info['rent_date'])
        order_page.select_rent_period_in_order()
        order_page.select_black_color_in_order_page()
        order_page.add_text_element(ORDER_LOCATORS.COMMENTS_FIELD, order_info['comment'])
        order_page.click_order_button()
        order_page.click_yes()
        assert 'Заказ оформлен' in order_page.get_order_success()