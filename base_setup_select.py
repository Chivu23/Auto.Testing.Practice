# selenium si webdriver-manager -> library needs to be install
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# simple instantiation the browser
# driver = webdriver.Chrome()

# complex and recommended way to instantiation browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# access un link
LINK = "https://formy-project.herokuapp.com/"
driver.get(LINK)
time.sleep(3)

# max win
driver.maximize_window()
time.sleep(3)


# access link Autocomplete on the web page
autocomplete_link = driver.find_element(By.LINK_TEXT, "Autocomplete")
autocomplete_link.click()
time.sleep(3)

# go back ( or go black)
driver.back()
time.sleep(2)
