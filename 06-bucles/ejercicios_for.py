"""""
usuario=input("Escribe una palabra y la muestro 10 veces: ")
for i in range (10):
    print(usuario)

edad=int(input("Escribe tu edad: "))
for i in range (0, edad, 1):
    print(f"Has cumplido estosaños {i+1}")

numero = int(input("Escribe un número positivo y te doy los impares previas a él: "))
for i in range(1, numero+1, 2):
    print(f"Los impares son {i}")

num = int(input("Escribe un numero y hago la cuenta regresiva: "))
for i in range (num, -1, -1):
    print(i, end=", ")

inversion = float(input("Ingrese el capital a intervir: "))
interes = float(input("Ingrese el interés anual: "))
anios = int(input("Ingrese la cantidad de años: "))
for i in range (anios):
    inversion *= 1 + interes / 100
    print(f"El capital después de {anios+1} es: {inversion}")

triangulo = int(input("Ingresa la altura del triangulo: "))
for i in range (triangulo):
    for j in range(i+1):
        print("*", end ="")
    print("")

numero = int(input("Escribe la tabla a realizar: "))
for i in range(1, 11):
    resultado = numero *i
    print(f"El resultado de {numero} x {i} es: {resultado}")
"""

n = int(input("Ingresa un numero positiv para tener la altura del triangulo: "))
for i in range (1, n+1, 2):
    for j in range (i, 0, -2):
        print(j, end=" ")
    print("")
