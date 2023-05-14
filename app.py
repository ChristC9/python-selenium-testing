from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os

username = os.environ.get("username")
pw = os.environ.get("pw")
link = os.environ.get("url")


chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument(
    r"--user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data\Default")

# Ignore SSL errors
chrome_options.add_argument("--ignore-certificate-errors")

# Set up the Selenium driver
driver = webdriver.Chrome(options=chrome_options)


driver.get(link)
time.sleep(25)
username_input = driver.find_element(By.NAME, "Username")
password_input = driver.find_element(By.NAME, "Password")

username_input.send_keys(username)
password_input.send_keys(pw)
submit_button = driver.find_element(By.NAME, "Sign In")
submit_button.click()

input("Press Enter to continue...")

driver.quit()
