from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pytest

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.mark.parametrize('ananaswer', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, ananaswer):
    link= f"https://stepik.org/lesson/{ananaswer}/step/1"
    browser.get(link)
    browser.implicitly_wait(20)
    a= math.log(int(time.time()))
    x='yaroslavmaslov0951@gmail.com'
    y='050895ASdf'
    
    aut=browser.find_element(By.ID, value='ember33').click()
    email=browser.find_element(By.ID, value='id_login_email')
    email.send_keys(x)
    pas=browser.find_element(By.ID, value='id_login_password')
    pas.send_keys(y)
    button= browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader ").click()
    browser.implicitly_wait(20)
    answer=browser.find_element(By.TAG_NAME, value='textarea')
    answer.send_keys(a)
    browser.implicitly_wait(20)
    button= browser.find_element(By.CLASS_NAME, "submit-submission").click()
    message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    assert "Correct!" in message.text
