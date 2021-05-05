nombre = "Luis Juárez"

#funciones generales
print(type(nombre))

#detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")


#Limpiar espacios
frase = "    mi contenido    d  "
print(frase)
print(frase.strip())


#Eliminar variables
year = 2020
print(year)
del year
#print(year)

#Comprobar variables vacias
texto = "  ff  "
if len(texto) <= 0:
    print("La variable está vaciía")
else:
    print(f"La variable tiene contenido" , len(texto))


#Encontrar caracteres de un string
frase = "La vida es bella"
print(frase.find("vida"))


#Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

#Procesar mayusculas y minisculas
print(nombre)
print(nombre.lower())
print(nombre.upper())