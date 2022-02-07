from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/Test.html")
# driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\Test.html")
driver.find_element_by_id("clickOnMe").click()
# driver.find_element_by_tag_name("p").click()
driver.switch_to.alert.accept()
driver.find_element_by_id("clickOnMe").click()
driver.switch_to.alert.dismiss()
driver.find_element_by_id("fname").send_keys("Ola")     #wprowadza wartosc do poola tekstowego
# driver.find_element_by_name("password").send_keys(Keys.ENTER)    #symuluje naciskanie konkretnych klawiszy na klawiaturze

#select w liscie rozwijanej
auto_select = Select(driver.find_element_by_tag_name("select"))
auto_select.select_by_visible_text("Volvo")
auto_select.select_by_value("saab")
auto_select.select_by_index(0)

#zaznaczanie checkboxa
driver.find_element_by_xpath("//input[@type='checkbox']").click()

#zaznaczanie radio buttona
driver.find_element_by_xpath("//input[@value='male']").click()

#pobieranie tekstu z elementu
print(driver.find_element_by_xpath("//input[@value='male']").text)   #nie ma tekstu, powinno zwrocic sie puste
print(driver.find_element_by_tag_name("h1").text)
print(driver.find_element_by_id("clickOnMe").text)
print(driver.find_element_by_tag_name("p").text)    #puste, bo ukryty element

#Pobieranie tekstu z ukrytego elementu
print(driver.find_element_by_tag_name('p').get_attribute('textContent'))
print("Brak tekstu" + driver.find_element_by_name("fname").text)    #wyciagniecie tej wartosci, nic sie nie wyswietla
print("Z tekstem: " + driver.find_element_by_name("fname").get_attribute('value'))

#sprawdzenie czy obrazek wyswietla sie na stronie
print(driver.find_element_by_id("smileImage").size.get("height"))
print(driver.find_element_by_id("smileImage").get_attribute("naturalHeight"))    #jesli zero to sie nie wyswietla sie obrazek

#przelaczanie do nowo otwartego okna
driver.find_element_by_id('newPage').click()
print(driver.title)
current_window_name = driver.current_window_handle
window_names = driver.window_handles
for window in window_names:
    if window != current_window_name:
        driver.switch_to.window(window)
print(driver.title)
driver.switch_to.window(current_window_name)
print(driver.title)

driver.quit()