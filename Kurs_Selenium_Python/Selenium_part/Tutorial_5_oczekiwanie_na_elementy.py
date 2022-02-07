from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
path = os.path.abspath("./Resources/Waits.html")
driver.get(path)

#metoda sleep
# driver.find_element_by_id("clickOnMe").click()
# time.sleep(5)
# print(driver.find_element_by_tag_name('p').text)    #ten tekst pojawia sie po czasie, wczesniej jest hidden

#implicit wait
# driver.implicitly_wait(10)    #jest definiowana dla kazdego szukanego elementu w skrypcie, nie dla konkretnej akcji
# driver.find_element_by_id("clickOnMe").click()
# print(driver.find_element_by_tag_name('p').text)

#explicit wait - WebDriverWait
path = os.path.abspath("./Resources/Waits2.html")
driver.get(path)
wait = WebDriverWait(driver, 10, 0.5)
driver.find_element_by_id("clickOnMe").click()
# wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, 'p')))
# print(driver.find_element_by_tag_name('p').text)

'''explicit wait - definiowanie wlasnego warunku (LAMBDA)
Aby stworzyć własny warunek dla WebDriverWait możemy również stworzyć klasę zawierającą metodę __call__ która jako 
parametr przyjmuje drivera i zawiera w swoim ciele warunek który będzie sprawdzany:
class WaitForListSize:
    def __init__(self, locator, ezpected_size):
        self.locator = locator
        self.expected_size = expected_size
    def __cal__(self, driver):
        return len(driver.find_element_by_xpath(self.locator)) == self.expected_size
'''
wait.until(lambda wd: len(wd.find_elements_by_tag_name("p")) == 1)
print(driver.find_element_by_tag_name('p').text)