"""
FOR

for variable in elemento_iterable (lista, rango, etc)
    bloque de instrucciones

"""
contador = 0
resultado = 0
for contador in range(0, 10):
    print("Voy por el " + str(contador))

    resultado += contador

print(f"El resultado es: {resultado}")

#EJEMPLO TABLAS DE MULTIPLICAR
print("## Ejemplo Tablas ##")

numero_usuario = int(input("De qué numero quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"Tabla de multiplicar del numero {numero_usuario} ")

for numero_tabla in range (1, 11):
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada")

