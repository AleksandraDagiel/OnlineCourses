from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import *

driver = webdriver.Chrome(ChromeDriverManager().install())

'''
Sprawdzenie czy element jest enabled
Jesli element jest disabled a probujemy wprowadzic wartosc otrzymamy blad 'ElementNotInteractableExeption'
'''

driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/Test.html")
# driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\Test.html")
first_name_input = driver.find_element_by_id("fname")

if first_name_input.is_enabled():
    first_name_input.send_keys("olololo")
else:
    print("Element nie jest dostepny")

'''Sprawdzenie czy element jest wyswietlony'''

paragraph = driver.find_element_by_tag_name('p')

if paragraph.is_displayed():
    print('Is displayed: ')
    print(paragraph.text)
else:
    print('Is not displayed: ')
    print(paragraph.get_attribute("textContent"))

'''
Sprawdzenie czy element istnieje na stronie
- metoda find element w przypadku brzaku wykrycia elementu wywala blad
- metoda find elements zwraca po prostu pusta liste
'''

elements = driver.find_elements_by_tag_name("paaa")

if len(elements) > 0:
    print("Element istnieje na stronie")
else:
    print("Brak elementu na stronie")
try:
    driver.find_element_by_tag_name("papa")
    print("Element istnieje")
except NoSuchElementException:
    print("Element nie isnieje")


'''Sprawdzenie czy element jest wybrany/zaznaczony'''

checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")
checkbox.click()
if checkbox.is_selected():
    print("Wartosc jest zaznaczona. Odznaczam...")
    checkbox.click()
else:
    print("Zaznaczam wartosc")
    checkbox.click()

driver.quit()