
import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# create driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 1. open link : https://demo.nopcommerce.com/
LINK = "https://demo.nopcommerce.com/register?returnUrl=%2F"
driver.get(LINK)
time.sleep(1)
driver.maximize_window()

"""
CLASS NAME SELECTOR:
- use for identify HTML elem with class attribute
- class attribute is use to group elem by common characteristics
"""

# identify div that contain "Your Personal Details" text
# [class="title"]

element1 = driver.find_element(By.CLASS_NAME, "title")