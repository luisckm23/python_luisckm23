cantantes = ["2Pac", "Drake", "Julio Iglesias", "Chocho"]
numeros = [1, 2, 5, 8, 8, 3, 4]

# Ordenar una lista
print(numeros)
numeros.sort()
print(numeros)

# Agregar elementos dentro de una lista
cantantes.append("Natos")
cantantes.insert(2, "Bisbal") #Este metodo espera dos parametros
print(cantantes)

# Eliminar elementos de una lista
cantantes.pop(2) #Eliminar por numero de indice
cantantes.remove("Drake") #Eliminar por nombre concreto
print(cantantes)

#Dar la vuelta a una lista
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('Drake' in cantantes)

# Contar elementos
print(cantantes)
print(len(cantantes))

# Cuantas veces se repite un elemento en una lista
numeros.append(8)
print(numeros.count(8))

# Conseguir un indice
print(cantantes.index("2Pac"))

# Unir Listas
cantantes.extend(numeros)
print(cantantes)
