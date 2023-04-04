from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book").click()
    submit_button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    x_element = browser.find_element(by='id', value="input_value")
    x = x_element.text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    answer=browser.find_element(by='id', value='answer')
    answer.send_keys(y)
   
    submit_button.click()
    
finally:
    time.sleep(10)
    
    browser.quit()
