import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = str(math.log(abs(12*math.sin(int(x_element.text)))))
    browser.find_element(By.ID, "answer").send_keys(x)
    
    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    
    browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()
    
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
