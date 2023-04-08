from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pytest


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_get_basket_button(browser):
    browser.get(link)
    basket_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert basket_button, 'Basket button not found'
    time.sleep(30)
