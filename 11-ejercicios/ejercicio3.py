"""
Hacer un programa que compruebe si una variable esta vacia
y si esta vacía, rellenarla con texto y mostrarlo en mayúsculas

"""

texto = ""

if len(texto.strip()) <= 0:
    texto = "hola soy un texto en minusculas"
    print(texto.upper())

else:
    print(f"La variable tiene contenido: {texto}")