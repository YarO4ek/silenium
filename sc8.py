from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(by='id', value="input_value")
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    answer=browser.find_element(by='id', value='answer')
    answer.send_keys(y)
    
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
