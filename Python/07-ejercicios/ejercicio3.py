"""
Mostrar los cuadrados (numero multiplicado por si mismo) de los primeros 60 números naturales
Resolver con for y while
"""
print("### F O R ###")
resultado = 0

for contador in range(1, 61):
    cuadrado_dos = contador * contador
    print(f"Este es el cuadrado {cuadrado_dos} de {contador}")


print("\n### W H I L E ###")
counter = 0

while counter <= 60:
    cuadrado = counter * counter
    print(f"El cuadrado de {counter} es: {cuadrado}")
    counter +=1