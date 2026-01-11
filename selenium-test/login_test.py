from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

email = ''.join(random.choices(string.ascii_lowercase, k=6)) + "@test.com"
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# Selenium Manager automatically handles ChromeDriver
driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/login")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.NAME, "email").send_keys(email)
driver.find_element(By.NAME, "password").send_keys(password)

time.sleep(2)
driver.quit()
