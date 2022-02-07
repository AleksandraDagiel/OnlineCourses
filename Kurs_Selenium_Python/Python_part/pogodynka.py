"""
if __name__ == '__main__':
powoduje, że nie ma printow w importowanym pliku
"""

def pogoda_krakow():
    return "Slonecznie"

def pogoda_szczecin():
    return "Pochmurno"

def pogoda_wroclaw():
    return "Upal"

if __name__ == '__main__':
    print(pogoda_krakow())
    print(pogoda_szczecin())
    print(pogoda_wroclaw())