"""
Las LISTAS son una colección de datos bajo un mismo nombre.
Para acceder a esos valores usamos un INDICE numérico

"""

pelicula = "Batman"

# Definir una lista
peliculas = ["Batman", "Spiderman", "ESDLA"]
cantantes = list(("2Pac", "Drake", "JLO")) #Se debe hacer tupla con doble paréntesis
years = list((range(2020, 2050)))
variada = ["Victor", 1, 4.4, True, "Texto"]

"""
print(pelicula)
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

# INDICES
peliculas[1] = "Gran Torino" #Cambianos el índice que elijamos por otro
print(peliculas) #Cambianos el índice que elijamos por otro

print(peliculas[1]) #Obtenemos el indice dentro de la lista
print(peliculas[-2]) #Obtenemos el indice dentro de la lista de atrás a adelante
print(cantantes[1:3]) #Obtenemos los indices en un rango
print(cantantes[2:]) #Obtenemos los índices del que elijamos al último

# Añadir elementos a lista
cantantes.append("Kase O")
cantantes.append("K ase O")
print(cantantes)

#Recorrer una lista con el ciclo FOR
"""
nueva_peli = ""

while nueva_peli != "parar":
    nueva_peli = input("Escribe una una pelicula a la lista: ")

    if nueva_peli != "parar":
        peliculas.append(nueva_peli)

print("L I S T A D O    D E    P E L I C U L A S")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)}. {pelicula}") #Con esto recorremos un índice y le señalamos #que número de índice le corresponde 
"""

# Listas multidimensionales 

print("\n # # # Lista de contactos # # #")

contactos = [ 
    [
        'Antonio',
        'antonio@anotnio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Joel',
        'joel@joel.com'
    ]
]

#print(contactos[1][1]) #Así obtenemos el contacto de Luis, que está en el índice 1 y subíndice 1

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("E-mail: " + elemento)
    print("\n")