from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(by='id', value='input_value')
    x = x_element.text
    y = calc(x)
    answer=browser.find_element(by='id', value='answer')
    answer.send_keys(y)
    checkbox=browser.find_element(by='id', value='robotCheckbox')
    checkbox.click()
    radio=browser.find_element(by='id', value='robotsRule')
    radio.click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
