from io import open
import pathlib
import shutil

# Abrir archivo
ruta = str(pathlib.Path().absolute()) +"/fichero_texto.txt"
archivo = open(ruta, "a+")

# Escribir dentro del archivo
archivo.write("Soy un texto escrito desde Python\n")

# Cerrar archivo
archivo.close()

# Leer archivo
ruta = str(pathlib.Path().absolute()) +"/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
#contenido = archivo_lectura.read()

#for elemento in contenido:
 #   print(contenido)

# Leer contenido y guardarlo en una LISTA
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    if  not frase.isnumeric():
        print(" - "+frase.upper())

# Copiar
#ruta_original = str(pathlib.Path().absolute()) +"/fichero_texto.txt"
#ruta_nueva = str(pathlib.Path().absolute()) +"/fichero_copiado.txt"
#ruta_alternativa = str(pathlib.Path().absolute()) +"./14-sistemaArchivos/fichero_copiado.txt"

#shutil.copyfile(ruta_original, ruta_alternativa)

# Mover un archivo a otro
"""
ruta_original = str(pathlib.Path().absolute()) +"/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) +"/fichero_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)
"""

# Eliminar ficheros
import os
"""
ruta_nueva = str(pathlib.Path().absolute()) +"/fichero_NUEVO.txt"

os.remove(ruta_original)
"""
#Comprobar si un archivo existe
import os.path

#print(os.path.abspath("../"))
ruta_comprobar = os.path.abspath("./")+ "/fichero_texto.txt"
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")
