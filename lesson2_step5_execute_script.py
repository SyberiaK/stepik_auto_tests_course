import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_elem = int(browser.find_element(By.ID, "input_value").text)
    x = str(math.log(abs(12*math.sin(x_elem))))
    browser.find_element(By.CSS_SELECTOR, "input[type=text]").send_keys(x)
    
    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    
    radio = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
