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
