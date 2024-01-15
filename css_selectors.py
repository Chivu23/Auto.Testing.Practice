"""
CSS SELCTORS ___ un sir de caractere utilizat pentru a identifica elemente in codul HTML
                cu sopul de a putea interactiona cu acestea si de a le verifica functionalitatea
CSS SELECTORS fata de XPATH sunt mai eficienti dpdv al codului,
insa interactioneaza cu elementele doar de sus in jos in structura pag HTML.
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
time.sleep(1)

LINK = "https://the-internet.herokuapp.com/login"
driver.get(LINK)
time.sleep(1)

driver.maximize_window()
time.sleep(1)

# Identify - ID -
# identificarea inputului username dupa ID, utilizand CSS SELECTOR

username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith")
time.sleep(1)

# Identify - CLASS

# a. identif. elem h4 dupa clasa folosind CSS SELECTOR
h4_element = driver.find_element(By.CSS_SELECTOR, ".subheader")

# b. identif.  primului elem cu clasele large-6, small-12, columns, folosind CSS SELECTOR.
# Folosind assert, verif tag.ul acestuia este div.

# class1.class2.class3
elem = driver.find_element(By.CSS_SELECTOR, ".large-6.small-12.columns")
assert elem.tag_name == "div"

# CSS SELECTOR - identificare dupa nume tag + id/clasa

# a. Identifica elementul form, dupa tag + id, folosind CSS SELECTOR.
# Verifica ca atributul method al acestuia are valoarea 'post'

# a.
form_elem = driver.find_element(By.CSS_SELECTOR, " form#login")
expected = "post"
actual = form_elem.get_attribute("method")
assert expected == actual

# b. Identifica butonul de login dupa tag + clasa, folosind CSS SELECTOR.
# Verifica ca textul acestuia este 'Login'
button_login = driver.find_element(By.CSS_SELECTOR, "button.radius")
expected = "Login"
actual = button_login.text
assert actual == expected

# 4 . CSS SELECTOR - identificare dupa tip atribut=valoare
# Identifica labelul pentru parola dupa atribut=valoare, folosind CSS SELECTOR.
# Verifica ca textul acestuia este cel asteptat.

# VAR 1   - *[for="password"] - cauta orice elem(indiferent de tag) care are atributul
# for cu valoarea 'password'

# VAR 2   - label[for="password"]  -  cauta elemente sau elementul cu tag.ul label care are
# atributul for cu valoarea "password"

label_elem = driver.find_element(By.CSS_SELECTOR, "label[for='password']")
expected_txt_label = "Password"
actual_text_label = label_elem.text

assert actual_text_label == expected_txt_label

"""
5. CSS SELECTOR - identificare element mergand din copil in copil (>)

Identifica link-ul din footer (Elemental Selenium), pornind de la div-ul
cu id-ul "page-footer" folosind CSS SELECTOR, si mergand din copil in copil.
Verifica ca valoarea atributului href este cea asteptata.
"""

footer_link = driver.find_element(By.CSS_SELECTOR, "div#page-footer>div>div>a")
expected_footer = "http://elementalselenium.com/"
actual_footer = footer_link.get_attribute("href")

assert expected_footer == actual_footer

"""
6. CSS SELECTOR - identificare orice copil

Identifica link-ul din footer (Elemental Selenium), pornind de la div-ul
cu id-ul "page-footer" folosind CSS SELECTOR, sarind direct la acesta.

Verifica ca tag-ul acestuia este un tag a
"""

footer_link2 = driver.find_element(By. CSS_SELECTOR, 'div#page-footer a')


"""
7. CSS SELECTOR - identificarea primului copil (first-of-type)

Identifica primul div ce apartine de tag-ul form si verifica ca are clasa row.
"""
# form > div:first-of-type

# identificare primul copil direct al
# elem din tag ul form care la randul lui are tag ul div

"""
8. CSS SELECTOR - identificarea ultimului copil (last-of-type)

Identifica copilul ultimului div ce apartine de tag-ul form
si verifica ca acesta are 3 clase setate.
"""
div_elem = driver.find_element(By. CSS_SELECTOR, 'form > div:last-of-type > div')
classes_as_str = div_elem.get_attribute('class')
classes_list = classes_as_str.split()
assert len(classes_list) == 3


"""
9. CSS SELECTOR - identificare copil care nu este nici primul, nici ultimul (nth-of-type)

Acceseaza elementul input se apartine de al doilea copil al elementului form
si verifica ca are id-ul setat corespunzator
"""

# form > *:nth-of-type(2) input
#form > *:nth-of-type(2) > div > input


"""
10. CSS SELECTOR - identificare frate ulterior (+)

Cauta elementul input care are ca si frate un label cu atributul for=username.

Verifica ca acesta are atributul type=text
"""
#  label[for="username"] + input

# FRATII ULTERIROI