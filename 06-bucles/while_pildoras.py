"""""
edad = int(input("Ingresa la edad, por favor: "))

while edad < 6 or edad >= 100:
    print("Es una edad incorrecta. Intentalo de nuevo")
    edad = int(input("Ingresa la edad, por favor: "))
print("Gracias por colaborar, puedes pasar")
print(f"Edad del aspirtante es {edad}")
"""


print("Programa de acceso")

password = input("Ingresa tu contraseña: ")
key = "luis"
intentos = 0

while password != key:
    print("Contraseña incorrecta")

    if intentos == 2:
        print("Has consumido demasiados intentos.")
        break
    password = input("Ingresa tu contraseña: ")
    if password != key:
        intentos = intentos + 1

if intentos < 2:
    print("Contraseña correcta, adelante!")

print("Programa que dice cuántas veces aparece una letra dentro de una frase")

frase = input("Escribe una frase: ")
letra= input("Escribe la letra a contar: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print(f"La letra ''{letra}'' aparece {contador} veces en la frase ''{frase}'' ")