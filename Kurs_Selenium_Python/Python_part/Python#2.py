"""
Importowanie modułów
Generator liczb losowych
"""
import random

def generuj_liczbe(min, max):
    return random.randint(min, max)

for i in range(0,20):
    print(generuj_liczbe(0, 100))

"""
- Instalacja paczek przez Pythona
Settings -> Project -> Project Interpreter -> + szukana paczka   |    albo w cmd przez pip install nazwa
xlrd - paczka pomagajaca przy czytaniu excela
selenium
- sprawdzenie listy paczek:
pip list
- znalezienie paczki:
pip search nazwa
pip search selenium
- po zainstalowaniu pipem Pycharm nie widzi paczek i odwrotnie
Przy tworzeniu nowego projektu "Create Project" trzeba zaznaczyc ptaszka przy inherit global site-packages
"""
