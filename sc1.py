from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    firstname = browser.find_element(By.XPATH, "//div[@class='first_block']/div[contains(@class, 'first')]/input")
    firstname.send_keys("Yaroslav")
    lastname = browser.find_element(By.XPATH, "//div[@class='first_block']/div[contains(@class, 'second')]/input")
    lastname.send_keys("Maslov")
    email = browser.find_element(By.XPATH, "//div[@class='first_block']/div[contains(@class, 'third')]/input")
    email.send_keys("SPB")
    
   
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    
    time.sleep(1)

    
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    
    welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
