from selenium.webdriver.common.by import By


class MAIN_LOCATORS:
    BTN_COOKIE = (By.CLASS_NAME, 'App_CookieButton__3cvqF')
    LOGO_YA = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    LOGO_SAMO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')


class QUESTION:
    QUESTION = (By.ID, 'accordion__heading-{}')


class ANSWER:
    ANSWER = (By.ID, 'accordion__panel-{}')

class LOGO:
    YA_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR")
