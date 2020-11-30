#!/usr/bin/env python3
# -*- coding: utf-8 -*-

DRIVER='./chromedriver'
URL='http://192.168.10.1/login.html'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


chromeOptions = Options()
chromeOptions.headless = True


#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome(executable_path=DRIVER, options=chromeOptions) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(URL)
    driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys("sercomm")
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys("1234")
    #Usuario y contraseña incorrectos
    driver.find_element(By.CSS_SELECTOR, 'input[type="button"].button-apply-wide').click()
    print('Peticion:' + driver.page_source)
    first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "div#message-error-text")))
    print(first_result.text)
