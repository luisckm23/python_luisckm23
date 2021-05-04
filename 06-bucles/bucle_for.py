"""
FOR

for variable in elemento_iterable (lista, rango, etc)
    bloque de instrucciones

"""
contador = 0
resultado = 0

for contador in range (0, 10):
    print("Voy por el "+ str(contador))

    resultado += contador

print(f"El resultado es: {resultado}")


###Ejemplo tablas multiplicar 
print("\n#### Ejemplo T A B L A S #####")

numeroUsuario = int(input("De qué número quieres la tabla: "))

if numeroUsuario < 1:
    numeroUsuario = 1
print(f"\nTabla de multiplicar del numero {numeroUsuario}")

for numero_Tabla in range (1, 11):
    if numeroUsuario == 45:
        print("No se puede usar se numero")
        break
    
    print(f"{numeroUsuario} x {numero_Tabla} = {numeroUsuario * numero_Tabla}")
else:
    print("Tabla finalizada")