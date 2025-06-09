from selenium.webdriver.common.by import By

class ORDER_LOCATORS:
    BUTTON_ORDER_HEADER = (By.CSS_SELECTOR, "div.Header_Nav__AGCXC button.Button_Button__ra12g")
    NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    SURNAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    METRO_DROPDOWN = (By.CSS_SELECTOR, ".select-search__input")

    NEXT_BUTTON = (By.CSS_SELECTOR, 'button[class*="Button_Middle__1CSJM"]')

    RENT_DATE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
    RENT_TERMS_DROPDOWN = (By.CSS_SELECTOR, 'div[class="Dropdown-control"]')
    RENT_TERMS_4_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='четверо суток']")
    SCOOTER_COLOR_BLACK_CHECKBOX = (By.CSS_SELECTOR, "div.Order_Checkboxes__3lWSI #black")
    COMMENTS_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.CSS_SELECTOR, 'button[class="Button_Button__ra12g Button_Middle__1CSJM"]')
    COMPLITE_ORDER_MODAL = (By.XPATH, "//*[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and normalize-space(text())='Заказать']")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    ORDER_STATUS = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    BODY = (By.TAG_NAME, "body")

    @staticmethod
    def select_metro_station_option(metro):
        return (By.XPATH, f"//button[.='{metro}']")

