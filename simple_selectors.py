"""
SELECTORS:
-class-name
-name
-tag_name
"""

import time

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
time.sleep(1)

"""
CLASS NAME SELECTOR:
- use for identify HTML elem with class attribute
- class attribute is use to group elem by common characteristics
"""

# identify div that contain "Your Personal Details" text
# [class="title"]

element1 = driver.find_element(By.CLASS_NAME, "title")

# identifying several elements after a selector
div_element = driver.find_elements(By.CLASS_NAME, "title")
print(div_element)   # list of object type WebElem

assert len(div_element) == 9

# identifying an element that has the class attribute
# and they are awarded more than one class
# <ul class="top-menu notmobile">...</ul>

# 1
driver.find_element(By.CLASS_NAME, "top-menu")
# 2
driver.find_element(By.CLASS_NAME, "notmobile")


# NAME SELECTOR  -  USE WHEN WE NEED TO IDENTIFY HTML ELEM WITH ATTRIBUTE _NAME_
# -> identify input for "Newsletter" with name attribute

element_newsletter = driver.find_element(By.NAME, "Newsletter")


# TAG_NAME selector
#  -> not very use.

driver.find_element(By.TAG_NAME, "form")

div_list = driver.find_elements(By.TAG_NAME, "div")
print(len(div_list))

