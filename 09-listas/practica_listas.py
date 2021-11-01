miLista = ["María", "Pepe", "Martha", "Antonio"]
miLista2=["Sandra", "Lucía"]

#Metodo para agregar un elemento a la lista
print("\nMetodo append para agregar un elemento a la lista")
miLista.append("Luis")

#Metodo para insertar un elemento a la lista en determinado lugar
print("\nMetodo para insertar un elemento a la lista en determinado lugar de la lista")
miLista.insert(2,"Mario")

#Metodo para añadir elementos a una lista
print("\nMetodo extend para añadir elementos a una lista")
miLista.extend(["Ricardo", "Arturo"])

#Metodo para eliminar un elemento de la lista
print("\nMetodo remove para eliminar un elemento de la lista")
miLista.remove("María")

#miLista.pop()

miLista3= miLista+miLista2

print(miLista3[:])
print(miLista[:])
print(miLista.index("Antonio"))
print("Pepe" in miLista)