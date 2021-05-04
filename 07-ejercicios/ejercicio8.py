"""
Obtener el porcentaje requerido de un numero dadd

"""

numero = int(input("Ingresa el numero: "))
porcentaje = int(input(f"Ingresa el porcentaje a obtener de {numero}: "))

operacion = (numero * (porcentaje / 100))
print(f"{numero} con el {porcentaje}% aplicado es {numero - operacion}")