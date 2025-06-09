from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from urls import URL_BASE

class Base_page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие страницы")
    def go_to_url(self):
        self.driver.get(URL_BASE)
    @allure.step("Поиск элемента по локатору")
    def find_element(self, locator): 
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу")
    def click_element(self, locator): 
        self.wait.until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    @allure.step("Добавление текста")
    def add_text_element(self, locator, keys): 
        self.find_element(locator).send_keys(keys)

    @allure.step("Получение текста из элемента")
    def get_text_element(self, locator): 
        return self.find_element(locator).text

    @allure.step("Видимость элемента")
    def visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Форматирование локатора")
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    @allure.step("Получение урла")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание определённого количества открытых окон")
    def wait_for_number_of_windows_to_be(self, number):
        self.wait.until(EC.number_of_windows_to_be(number))

    @allure.step("Переключение на последнее открытое окно")
    def switch_to_last_opened_window(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])

    @allure.step("Проверка перехода на страницу")
    def wait_for_redirect(self, text):
        self.wait.until(EC.url_contains(text))

