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
LINK = "https://demo.nopcommerce.com/"
driver.get(LINK)
time.sleep(1)
driver.maximize_window()

# 2. check website title
expected_title = "nopCommerce demo store"
actual_title = driver.title
assert expected_title == actual_title

print(actual_title)

# 3. clik on "Register" button
register_element = driver.find_element(By.LINK_TEXT, "Register")  # identify by link_text
register_element.click()

# 4. select gender then check that the find element has the type attribute "radio" value
gender_input_element = driver.find_element(By.ID, "gender-male")  # identify by id

# check attribute elem html
assert gender_input_element.get_attribute("type") == "radio"

gender_input_element.click()
time.sleep(2)

# 5. identify the element where we can write the first name.
# check that the found element has the right tag and write a first name.

first_name_element = driver.find_element(By.ID, "FirstName")
first_name_element.click()

# check tag element
assert first_name_element.tag_name == "input"

first_name_element.send_keys("John")
time.sleep(2)

# 6. identify the elem where we can write last name.
# check his tag and write a last name.

last_name_element = driver.find_element(By.ID, "LastName")
last_name_element.click()

assert last_name_element.tag_name == "input"

last_name_element.send_keys("Smith")
time.sleep(2)

# 7. identify the elem where we can write email.
# check the value of name that attribute is ok and write the email

email_element = driver.find_element(By.ID, "Email")
email_element.click()

assert email_element.get_attribute("name") == "Email"


email_element.send_keys(f"john.smith{random.randint(1, 9999)}@gmail.com")
time.sleep(2)

# 8. identify the elem for pass and write (min 3)  same pass in both places.
# check error msg

passw_element = driver.find_element(By.ID, "Password")
# passw_element.click()
passw_element.send_keys("123")

confirm_pass_element = driver.find_element(By.ID, "ConfirmPassword")
# confirm_pass_element.click()
confirm_pass_element.send_keys("123")

msg_error_pass_element = driver.find_element(By.ID, "Password-error")
actual_error_text = msg_error_pass_element.text
expected_error_text = "Password must meet the following rules:\nmust have at least 6 characters"
assert actual_error_text == expected_error_text

# 9. delete the pass entered in point 6.
# enter a new pass with 10-character pass and
# enter a confirmation pass that does not coincide with initial one.
# press the REGISTER button and check the error msg.
passw_element.clear()
confirm_pass_element.clear()

passw_element.send_keys("0123456789")
confirm_pass_element.send_keys("123456")

button_register = driver.find_element(By.ID, "register-button")
button_register.click()

not_matching_err_element = driver.find_element(By.ID, "ConfirmPassword-error")

actual_error = not_matching_err_element.text
expected_error = "The password and confirmation password do not match."

assert actual_error == expected_error
time.sleep(2)

# 10. delete pass from point 7 and insert 2 same pass then push REGISTER button.
# check that the string "registerresult" is found in the url of the current page

passw_element.clear()
confirm_pass_element.clear()

passw_element.send_keys("123456")
confirm_pass_element.send_keys("123456")

print(f"BEFORE: {driver.current_url}")
button_register.click()

current_url = driver.current_url
print(f"AFTER: {driver.current_url}")

assert "registerresult" in current_url
time.sleep(2)


# 11. close browser
driver.quit()
