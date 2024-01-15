"""
1.
- Instantiaza un browser de Chrome.
- Acceseaza pagina https://the-internet.herokuapp.com/
- Maximizeaza fereastra
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# LINK = "https://the-internet.herokuapp.com/"
driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)

"""
2. Acceseaza link-ul Form Authentication, folosind un selector potrivit.
Incearca mai multe variante posibile.
"""

# link_element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Form')
# link_element.click()
# time.sleep(2)

link_element = driver.find_element(By.LINK_TEXT, 'Form Authentication')
link_element.click()
time.sleep(1)

"""
3. Identifica elementul ce contine textul "Login Page"
si verifica, folosind un assert, ca acest element are textul asteptat
"""
login_text = driver.find_element(By.TAG_NAME, "h2")
login_button = driver.find_element(By.CLASS_NAME, "radius")
assert login_text.text == "Login Page"
time.sleep(2)

"""
4. Identifica input-urile username si password,
introdu valori valide, si da click pe butonul login
"""
username_element = driver.find_element(By.ID, "username")
password_element = driver.find_element(By.ID, "password")
username_element.send_keys("tomsmith")
password_element.send_keys("SuperSecretPassword!")
time.sleep(1)
login_button.click()

"""
5. Verifica, folosind un assert ca ai ajuns pe pagina
https://the-internet.herokuapp.com/secure
"""

url = "https://the-internet.herokuapp.com/secure"
assert driver.current_url == "https://the-internet.herokuapp.com/secure"

"""
6. Da click pe butonul logout
"""

logout_btn = driver.find_element(By.LINK_TEXT, "Logout")
logout_btn.click()
time.sleep(2)

"""
7. Introdu un username corect si o parola incorecta.
Identifica mesajul care apare si verifica in cod ca acela este mesajul asteptat.
"""

username_input_element = driver.find_element(By.ID, 'username')
username_input_element.send_keys('tomsmith')

password_input_element = driver.find_element(By.ID, 'password')
password_input_element.send_keys('123')

login_btn = driver.find_element(By.CLASS_NAME, "radius")
login_btn.click()

error_elem = driver.find_element(By.ID, 'flash')
print(error_elem)

# var. 1

# expected
# expected_error = 'Your password is invalid!\n*'
# assert expected_error == error_elem.text

# var. 2
assert 'Your password is invalid!' in error_elem.text
time.sleep(2)

"""
8. Introdu un username corect.
Gaseste elementul cu tag-ul h4.
Ia textul de pe el si fa split dupa spatiu. Considera fiecare cuvant ca o potentiala parola.
Foloseste o structura iterativa prin care sa introduci rand pe rand parolele si sa apesi login
La final, testul trebuie sa printeze fie "Nu am reusit sa gasesc parola", fie "Parola secreta este 
[parola]"
"""

h4_elem = driver.find_element(By.TAG_NAME, "h4")
possible_pass = h4_elem.text.split()
print(possible_pass)

for pwd in possible_pass:
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")
    password = driver.find_element(By.ID, "password")
    password.send_keys(pwd)

    button = driver.find_element(By.CLASS_NAME, "radius")
    button.click()
    if driver.current_url == "https://the-internet.herokuapp.com/secure":
        print(f"Secret pass is {pwd}")
        break
else:
    print("No find the correct pass!")


#
# text = " Have a nice day and be a nice man"
# print(text.split())
