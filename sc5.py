from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    x_element = browser.find_element(by='id', value="input_value")
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    answer=browser.find_element(by='id', value='answer')
    answer.send_keys(y)
    checkbox=browser.find_element(by='id', value='robotCheckbox')
    checkbox.click()
    browser.execute_script("window.scrollBy(0, 100);")
    radio=browser.find_element(by='id', value='robotsRule')
    radio.click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
