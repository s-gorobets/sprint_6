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