from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    x_element= browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element= browser.find_element(By.ID, "num2")
    y = y_element.text         
    z = str(int(x) + int(y))
    z=str(z)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element= browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element= browser.find_element(By.ID, "num2")
    y = y_element.text         
    z = str(int(x) + int(y))
    z=str(z)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    
    # закрываем браузер после всех манипуляций
    browser.quit()
