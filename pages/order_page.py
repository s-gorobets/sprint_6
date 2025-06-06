from locators.order_page_locators import ORDER_LOCATORS
from pages.base_page import Base_page
from data.order_data import order_info
from selenium.webdriver.common.by import By
import allure

class OrderPage(Base_page):
    @allure.step("Нажатие на кнопку 'Заказать' в заголовке страницы")
    def clicl_to_order_button(self):
        self.click_element(ORDER_LOCATORS.BUTTON_ORDER_HEADER)

    @allure.step("Заполняем поле 'Имя' на странице заказа")
    def send_name_in_order_page(self, name):
        self.add_text_element(ORDER_LOCATORS.NAME_FIELD, name)

    @allure.step("Заполняем поле 'Фамилия' на странице заказа")
    def send_soname_in_order_page(self, soname):
        self.add_text_element(ORDER_LOCATORS.SURNAME_FIELD, soname)

    @allure.step("Заполняем поле 'Адрес' на странице заказа")
    def send_address_in_order_page(self, address):
        self.add_text_element(ORDER_LOCATORS.ADDRESS_FIELD, address)

    @allure.step("Выбираем станцию метро")
    def select_metro_station_in_order_page(self, metro):
        field_metro = self.find_element(ORDER_LOCATORS.METRO_DROPDOWN)
        field_metro.click()
        field_metro.send_keys(metro)

        self.find_element(ORDER_LOCATORS.select_metro_station_option(metro)).click()
    @allure.step("Заполняем поле 'Телефон'")
    def send_phone_in_order_page(self, phone):
        self.add_text_element(ORDER_LOCATORS.PHONE_NUMBER_FIELD, keys=phone)

    @allure.step("Переходим на вторую страницу заказа")
    def click_next_in_order_page(self):
        self.click_element(ORDER_LOCATORS.ORDER_BUTTON)

    @allure.step("Заполняем дату аренды")
    def select_date_start(self, rent_date):
        self.find_element(ORDER_LOCATORS.RENT_DATE_INPUT).send_keys(rent_date)
        self.click_element(ORDER_LOCATORS.BODY)

    @allure.step("Выбираем срок аренды")
    def select_rent_period_in_order(self):
        self.click_element(ORDER_LOCATORS.RENT_TERMS_DROPDOWN)
        self.click_element(ORDER_LOCATORS.RENT_TERMS_4_DAYS)

    @allure.step("Выбираем чёрный цвет самоката")
    def select_black_color_in_order_page(self):
        self.click_element(ORDER_LOCATORS.SCOOTER_COLOR_BLACK_CHECKBOX)
        
    @allure.step("Оставляем комментарий для курьера")
    def add_comment_for_courier(self, comment):  # Оставляем комментарий для курьера
        self.add_text_element(ORDER_LOCATORS.COMMENTS_FIELD, keys=comment)

    @allure.step("Нажимаем кнопку 'Заказать'")
    def click_order_button(self):
        self.click_element(ORDER_LOCATORS.COMPLITE_ORDER_MODAL)

    @allure.step("Нажать кнопку 'Да' в окне подтверждения заказа")
    def click_yes(self):
        self.find_element(ORDER_LOCATORS.BUTTON_YES).click()

    @allure.step('Получение текста сообщения об успешном заказе')
    def get_order_success(self):
        return self.get_text_element(ORDER_LOCATORS.ORDER_STATUS)


