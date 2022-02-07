import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

'''
- pip install pytest
- assert pozwala na sprawdzenie konkretnego warunku
- glupi interpreter ma problem z 2 pythonami:    python -m pytest Tutorial_6_Framework_PyTest.py
- puszcza wszystkie suity z pytestem
- pytest puszcza pliki tylko z "test" w nazwie pliku
- metoda musi rozpoczynac sie od slowa "test"
- "assert" translate: "dowiesc czegos" 
'''

def test_method():
    x = 5
    y = 2
    assert x + y == 7, "Assertion failed, Expected 7"
    assert x + y == 2, "Assertion failed, Expected 7"

'''Weryfikacja rezultatow asercje
- mozna sprawdzac wszystko co zwraca True/False
'''
driver = webdriver.Chrome(ChromeDriverManager().install())
def test_method():
    x = 5
    y = 2
    # assert driver.title == "Strona testowa", "Assertion failed, Expected 7"
    assert x + y == 7, "Assertion failed, Expected 7"
    assert x + y == 2, "Assertion failed, Expected 2 but was " + str(x + y)

""" Dekorator pytest fixtures, który umozliwia odpalenie kodu przed lub po tescie
@pytest.fixture()
yield 
"""
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    path = os.path.abspath("./Resources/Test.html")
    driver.get(path)
    driver.maximize_window()
    yield
    driver.quit()

def test_method(test_setup):
    assert driver.title == "Strona testowa"

""" 
Pytest parametrize:
- metoda zostaje odpalona kilkukrotnie dla roznych wartosci (lista krotek)
"""
@pytest.mark.parametrize("skladnik, suma", [(5, 10), (2, 5)])
def test_dodawanie(skladnik, suma):
    assert skladnik + skladnik == suma, "Suma dwoch takich samych skladnikow: " + str(skladnik) + " powinna byc rowna: " + str(skladnik + skladnik)

"""
Pytest:
- mark skip: pomijanie i oznaczane niedzialających testow, jesli nie chcemy puszczac testow, bo spodziewamy sie faila,
  np. blad srodowiskowy
- xfail : jesli wiemy o bledzie w aplikacji i nie zostal on jeszcze naprawiony
"""
@pytest.mark.skip
def test_method():
    x = 5
    y = 2
    assert x+y == 7, "Assertion failed, Expected 7"
    assert x+y == 2, "Assertion failed, Expected 2"

@pytest.mark.skip()
def test_method2():
    x = 5
    y = 2
    assert x+y == 7, "Assertion failed, Expected 7"
    assert x+y == 2, "Assertion failed, Expected 2"

@pytest.mark.xfail()
def test_method2():
    x = 5
    y = 2
    assert x+y == 7, "Assertion failed, Expected 7"
    assert x+y == 2, "Assertion failed, Expected 2"

"""
Uruchamianie kilku testow jednoczesnie
- instalacja pip install pytest-xdist
- py.test -n 3 (3 testy jednoczesnie)
"""

"""
Uruchamianie metod testowych z poziomu PyCharma
- PyCharm jako domyslny runner testow:
file -> settings - > tools -> python integrated tools -> testing -> default test runner: pytest
"""
