"""
Pedir dos numeros al usuario y hacer todas las operaciones básicas de una calculadora y mostrar 
el resultado
"""

numero1 = float(input("Ingresa un numero, por favor: "))
numero2 = float(input("Ingresa otro numero, por favor: "))

print("# # # C A L C U L A D O R A # # #")
print(f"La suma de {numero1} + {numero2} =  {numero1 + numero2}")
print(f"La resta de {numero1} - {numero2} = {numero1 - numero2}")
print(f"La multiplicacion de {numero1} x {numero2} = {numero1 * numero2}")
print(f"La división de {numero1} / {numero2} = {numero1 / numero2}")