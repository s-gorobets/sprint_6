from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from urls import URL_BASE

class Base_page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие страницы")
    def go_to_url(self): # переход по ссылке
        self.driver.get(URL_BASE)
    @allure.step("Поиск элемента по локатору")
    def find_element(self, locator): # поиск элемента
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Клик по элементу")
    def click_element(self, locator): # клик по элементу
        self.wait.until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    @allure.step("Добавление текста")
    def add_text_element(self, locator, keys): #добавление текста в элемент
        self.find_element(locator).send_keys(keys)

    @allure.step("Получение текста из элемента")
    def get_text_element(self, locator): # получение текста из элемента
        return self.find_element(locator).text

    @allure.step("Видимость элемента")
    def visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Форматирование локатора")
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

