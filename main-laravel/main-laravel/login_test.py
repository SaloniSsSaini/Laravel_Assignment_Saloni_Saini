import os
os.environ["WDM_LOCAL"] = "1"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

email = ''.join(random.choices(string.ascii_lowercase, k=6)) + "@test.com"
password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://127.0.0.1:8000/login")

time.sleep(2)
driver.find_element(By.NAME, "email").send_keys(email)
driver.find_element(By.NAME, "password").send_keys(password)

time.sleep(2)
driver.quit()
