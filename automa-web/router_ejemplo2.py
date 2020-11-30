from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Firefox() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("http://192.168.0.1/login.html")
    driver.find_element(By.CSS, 'input[type="text"]').send_keys("sercomm")
    driver.find_element(By.CSS, 'input[type="password"]').send_keys("1234")
    #Usuario y contraseña incorrectos
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "div#message>div#message-error>h2")))
    print(first_result.text)
