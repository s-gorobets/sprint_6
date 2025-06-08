from conftest import *
from pages.main_page import MainPage
import allure

class Test_Logo:
    @allure.title("Клик по логотипу Яндекса открывает Дзен")
    def test_yandex_logo_opens_dzen(self, driver):
        logo_ya = MainPage(driver)
        logo_ya.go_to_url()
        logo_ya.click_ya_logo()
        logo_ya.switch_to_new_window()
        assert logo_ya.wait_for_dzen_redirect()

    @allure.title("Клик по логотипу Cамоката открывает главную страницу")
    def test_logo_scooter_retur_main(self, driver):
        scooter_logo = MainPage(driver)
        scooter_logo.go_to_url()
        scooter_logo.click_order_button()
        scooter_logo.click_scooter_logo()
        actual = scooter_logo.get_current_url()
        exepted = URL_BASE
        assert actual == exepted
