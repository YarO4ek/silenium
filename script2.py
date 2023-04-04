from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    

    input1 = browser.find_element(by='name',value='first_name')
    print(input1)
    input1.send_keys("yaroslav")
    input2 = browser.find_element(by='name', value='last_name')
    print(input2)
    input2.send_keys("maslov")
    input3 = browser.find_element(by='class name', value='city')
    print(input3)
    input3.send_keys("Petroskoi")
    input4 = browser.find_element(by='id',value='country')
    print(input4)
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "//form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
