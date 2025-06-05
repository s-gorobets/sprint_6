import pytest
from urls import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locator_main import *

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

# @pytest.fixture()
# def cookie_click(driver):
#     wait = WebDriverWait(driver, 10)
#     driver.get(URL_BASE)
#     wait.until(EC.element_to_be_clickable(QUESTION.BTN_COOKIE)).click()

