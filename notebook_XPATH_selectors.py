"""
XPATH

XPATH = Selector to navigate in a HTML code

We can Use XPATH when none of the other variants of identification could not help
us find an element.

Types of XPATH :

1. Absolute XPATH:     -----   NOT RECOMMENDED  ------
- identify the element starting from the beginning of the doc up to the
point where the element is identified
- right click on the element, copy and then select full xpath
- example: /html/body/div[1]/div/div/div[2]/div[4]/div/form/div[3]/button
- start with a single slash "/" to mark reading from the beginning of the doc

2. Relative XPATH:
- identify the elem starting from the first unique elem found and navigating
forward or backward until we arrive where we need.
- right click on the elem, copy, select xpath
- example: //button[@type='submit' and @name='login-button']
- starting with two slash "//" to mark reading from inside the doc from a certain position

"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
time.sleep(1)

# access site
LINK = "https://the-internet.herokuapp.com/login"
driver.get(LINK)
time.sleep(1)

# ---> searching by tag

# //h4
# //form
# //input
# //form/div/div/input
# //form//input
element = driver.find_element(By.XPATH, "//h4")
elem = driver.find_element(By.XPATH, "form")


"""
---> searching by attribute =  value for a specif tag
//input[@name="username"]
//input[@type='text']
//input[@type='text' and @name='username']

---> searching after attribute = value non specif tag
//*[@type='text' and @name="username"]
"""


