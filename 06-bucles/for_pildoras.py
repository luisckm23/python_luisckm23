for i in ["primavera", "verano", "otoño", "invierno"]:
    print(i)

for i in ["Pildoras", "Informáticas", 3]:
    print("Hola", end=" ")


contador = 0
miEmail = input("Introduce tu direccion de e-mail: ")

for i in miEmail:
    if(i== "@" or i=="."):
        contador=contador+1

if contador == 2:
    print("El correo es correcto")
else:
    print("El correo no es correcto")


for i in range (5, 50, 3):
    print(f"El valor de la variable es: {i}")