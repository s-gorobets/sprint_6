from locators.locator_main import QUESTION, ANSWER, MAIN_LOCATORS, LOGO
from locators.order_page_locators import ORDER_LOCATORS
from pages.base_page import Base_page
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Base_page):
    @allure.title("Кликаем на Куки")
    def click_to_cookie(self,):
        self.click_element(MAIN_LOCATORS.BTN_COOKIE)

    @allure.title("Проверка блока FAQ")
    def get_question_and_answer(self, num):
        locator = self.format_locators(QUESTION.QUESTION, num)
        self.click_element(locator)
        return self.get_text_element(self.format_locators(ANSWER.ANSWER, num))

    @allure.step("Клик на лого Яндекса")
    def click_ya_logo(self):
        self.wait.until(EC.element_to_be_clickable(LOGO.YA_LOGO)).click()

    @allure.step("Клик на лого Скутера")
    def click_scooter_logo(self):
        self.wait.until(EC.element_to_be_clickable(LOGO.SCOOTER_LOGO)).click()

    @allure.step("Клик на кнопку заказа")
    def click_order_button(self):
        self.click_element(ORDER_LOCATORS.BUTTON_ORDER_HEADER)

    @allure.step("Получение урла")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переход на соседнюю вкладку")
    def switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)

    @allure.step("Проверка перехода на dzen.ru")
    def wait_for_dzen_redirect(self):
        self.wait.until(EC.url_contains("dzen.ru"))
        return "dzen.ru" in self.driver.current_url





