import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# create driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 1. open link : https://demo.nopcommerce.com/
LINK = "https://demo.nopcommerce.com/"
driver.get(LINK)
time.sleep(2)

# 2. check website title
expected_title = "nopCommerce demo store"
actual_title = driver.title
assert expected_title == actual_title

print(actual_title)

# 3. clik on "Register" button
register_element = driver.find_element(By.LINK_TEXT, "Register")   # identify by link_text
register_element.click()

# 4. select gender then check that the find element has the type attribute "radio" value
gender_input_element = driver.find_element(By.ID, "gender-male")  # identify by id

# check attribute elem html
assert gender_input_element.get_attribute("type") == "radio"

gender_input_element.click()
time.sleep(2)

# 5. identify the element where we can write the first name.
# check that the found element has the right tag and write a first name.

register_element = driver.find_element(By.ID, "FirstName")
register_element.click()
register_element.send_keys("John")
time.sleep(2)