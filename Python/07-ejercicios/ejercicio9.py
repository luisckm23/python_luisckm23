"""
Hacer un programa que pida numeros al usuario indefinidamente hasta meter el numero 111

"""
contador = 1

while contador < 111:
    numero = int(input("Ingresa un numero: "))
    if numero == 111:
        break
    else: 
        print(f"Has ingresado el numero {numero}")