from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

''' 
Notatki:
- narzedzie developerskie do odnajdywania elementow: F12
- driver = webdriver.Chrome(r"..\drivers\chromedriver.exe")     zamiast pobierać webdriver [pip install webdriver_manager
- metoda close zamyka tylko okno, na ktorym byl focus, a metoda quit zamyka wszystkie
#Find element by Id - 2 formy szukania. Przy samym find element trzeba zaimportowac biblioteke By
#Find element by name
#Lokalizowanie za pomoca tekstu linka
#Lokalizowanie za pomoca nazwy klasy
- moze byc wiecej elementow w klasie; mozna zlokalizowac oba elementy, mozna uzywac nazw przemiennie
#Lokalizowanie za pomoca nazwy tagu
- grupowanie, raczej nie ma unikalnych elementow raczej
# Lokalizowanie za pomoca selektorow CSS - docx w Resources
# Lokalizowanie za pomoca XPath
# Kopiowanie selektorow CSS i XPath
# Listy elementow na stronie
- jesli nie wyciagamy listy a pojedynczy tag, kiedy jest ich wiecej to bedzie zwrocony pierwszy pasujacy tag
'''
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/Test.html")
# driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\Test.html")
driver.maximize_window()
# driver.find_element_by_id("clickOnMe").click()
driver.find_element_by_id("clickOnMe")
driver.find_element(By.ID, "clickOnMe")
driver.find_element_by_name("fname")
driver.find_element_by_link_text('Visit W3Schools.com!')
driver.find_element_by_partial_link_text('Visit W3Schools')
driver.find_elements_by_class_name('topSecret')
driver.find_element_by_tag_name('a')    #a link
driver.find_element_by_tag_name('p')    #p paragraf
driver.find_element_by_tag_name('label')

#CSS
print(driver.find_element_by_css_selector('a').text)
print(driver.find_element_by_css_selector('img#smileImage').text)    #elementy z tagiem img i id smileImage
print(driver.find_element_by_css_selector('p.topSecret').text)   #elementy z tagiem p i klasa topSecret
print(driver.find_element_by_css_selector('th:first-child').text)

#XPath
print(driver.find_element_by_xpath('/html/body/table/tbody/tr/th'))
print(driver.find_element_by_xpath('//tbody//th'))
print(driver.find_element_by_xpath('//th'))
print(driver.find_element_by_xpath("//th[text()='Month']"))
print(driver.find_element_by_xpath('//button[@id="clickOnMe"]'))
print(driver.find_element_by_xpath('//input[@id="fname"]/following-sibling::table'))

#Listy elementow
elements_list_lenght = len(driver.find_elements_by_xpath('//th'))
print(elements_list_lenght)

driver.close()