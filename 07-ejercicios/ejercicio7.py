"""
Hacer un programa que muestre los numeros impares entre dos numeros que decida el usuario

"""
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

if numero1 < numero2:

    for contador in range (numero1, numero2):

        if contador % 2 == 0:
            print(f"El numero {contador} es par")
        else:
            print(f"El numero {contador} es impar")
else:
    print("El primer numero debe ser mayor al segundo")