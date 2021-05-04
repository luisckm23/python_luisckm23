"""
WHILE

Estructura de control que itera o repite la ejecucion de una serie de instrucciones, tantas veces como
sea necesario, hasta que deje de cumplirse la instruccion

while condicion:
    bloque de instrucciones
    actualizacion de contador

"""
contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador +=1

print("\n#### E J E R C I C I O    D O S ###")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador +=1

print(f"{muestrame}")

print("\n#### E J E R C I C I O    T R E S ###")

numeroUsuario = int(input("De qué numero quieres la tabla: "))

if numeroUsuario < 1:
    numeroUsuario = 1

print(f"### Tabla del {numeroUsuario}")

contador = 1

while contador <= 10:
    print(f"{numeroUsuario} x {contador} = {numeroUsuario * contador}")
    contador += 1
else:
    print("Tabla terminada")
