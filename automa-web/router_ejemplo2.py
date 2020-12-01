#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

pip install selenium

"""

IP="192.168.0.1"
USER=""
PASSWORD=""

DRIVER='./chromedriver'
URL_LOGIN="http://{0}/login.html".format(IP)
URL_RESTART="http://{0}/status-and-support.html#sub=41".format(IP)
SELECTOR_RESTART_ID="restartB"
SELECTOR_APPLY="applyButton"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import time

chromeOptions = Options()
chromeOptions.headless = True


#This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome(executable_path=DRIVER, options=chromeOptions) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get(URL_LOGIN)
    driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(USER)
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(PASSWORD)
    #Usuario y contraseña incorrectos
    driver.find_element(By.CSS_SELECTOR, 'input[type="button"].button-apply-wide').click()
    driver.save_screenshot('01_login.png')

    w = wait.until(presence_of_element_located((By.ID, "content")))

    driver.get(URL_RESTART)

    w = wait.until(presence_of_element_located((By.ID, SELECTOR_RESTART_ID)))
    driver.save_screenshot('02_restart.png')
    driver.find_element_by_id(SELECTOR_RESTART_ID).click()

    time.sleep(10.0)

    w = wait.until(presence_of_element_located((By.ID, SELECTOR_APPLY)))
    driver.save_screenshot('03_apply.png')
    driver.find_element_by_id(SELECTOR_APPLY).click()

    time.sleep(60.0)

    driver.save_screenshot('04_reboot.png')
    #
    #print(first_result.text)
