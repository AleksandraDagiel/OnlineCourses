from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

driver = webdriver.Chrome(ChromeDriverManager().install())

#obsluga iframe - strona wewnatrz strony
driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/iFrameTest.html")
# driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\iFrameTest.html")
print("before window switch: " + (driver.find_element_by_tag_name('h1').text))
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
print("after window switch: " + (driver.find_element_by_tag_name('h1').text))
driver.switch_to.default_content()
print("and back to first window: " + (driver.find_element_by_tag_name('h1').text))
driver.close()

#klikanie na element i ustawianie wartosci pola tekstowego - za pomoca JavaScript
driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/Test.html")
# driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\Test.html")
wartosc = "Ola"
driver.execute_script("arguments[0].setAttribute('value', '" + wartosc + "')", driver.find_element_by_id("fname"))
driver.execute_script("arguments[0].click();", driver.find_element_by_id("newPage"))

#symulowanie podwojnego klikniecia myszki
driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/DoubleClick.html")
# driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\DoubleClick.html")
button = driver.find_element_by_id("bottom")
webdriver.ActionChains(driver).double_click(button).perform()
time.sleep(3)
driver.close()

#usuwanie danych z pola tekstowego - bo inaczej dopisuje do tego, co jest
driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/Test.html")
# driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\Test.html")
username_input = driver.find_element_by_name("username")
username_input.send_keys("Ponury Adam")    #dopisuje
username_input.clear()
username_input.send_keys("Ponury Adam")
time.sleep(3)

# #symulowanie klikniecia prawym przyciskiem myszki
driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/DoubleClick.html")
# driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\DoubleClick.html")
button = driver.find_element_by_id("bottom")
webdriver.ActionChains(driver).context_click(button).perform()

# najechanie na element - hover\
driver.get("https://www.w3schools.com/")
# driver.get("https://www.w3schools.com/")

tutorial_element = driver.find_element_by_id("navbtn_tutorials")
webdriver.ActionChains(driver).move_to_element(tutorial_element).perform()


# symulowanie drag i drop
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")
# driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")
draggable = driver.find_element_by_id("draggable")
drop_target = driver.find_element_by_id("droptarget")
webdriver.ActionChains(driver).drag_and_drop(draggable, drop_target).perform()

# lancuchy akcji: najechanie na element i klikniecie
driver.get("https://www.w3schools.com/")
# # driver.get("https://www.w3schools.com/")
#
tutorial_element = driver.find_element_by_id("navbtn_tutorials")
webdriver.ActionChains(driver).move_to_element(tutorial_element).click().perform()

# #upload pliku i tworzenie screenshota - zrzut okna przegladarki
driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/FileUpload.html")
# driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\FileUpload.html")
upload_input = driver.find_element_by_id("myFile")
path = os.path.abspath("./Resources/uploadMe.txt")
driver.save_screenshot('Screenshots/before_upload.png')
upload_input.send_keys(path)
driver.save_screenshot('Screenshots/after_upload.png')

driver.quit()