import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "treasure")
    x = str(math.log(abs(12*math.sin(int(x_element.get_attribute("valuex"))))))
    browser.find_element(By.ID, "answer").send_keys(x)
    
    browser.find_element(By.ID, "robotCheckbox").click()
    
    browser.find_element(By.ID, "robotsRule").click()
    
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
