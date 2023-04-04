from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    

    input1 = browser.find_element(by='name',value='firstname')
    print(input1)
    input1.send_keys("yaroslav")
    input2 = browser.find_element(by='name', value='lastname')
    print(input2)
    input2.send_keys("maslov")
    input3 = browser.find_element(by='name',value='email')
    print(input3)
    input3.send_keys("yarko@gm.com")
    current_dir = os.path.abspath(os.path.abspath('srv'))
    file_name = "sto.txt"
    file_path = os.path.join(current_dir, file_name)
    send_file = browser.find_element(By.NAME, 'file')
    send_file.send_keys(file_path)
    
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
