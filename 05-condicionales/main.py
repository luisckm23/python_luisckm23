"""
Condicional IF

Si se cumple esta condicion
    Se ejecuta el grupo de instrucciones
SI NO
    Se ejecutan otras instrucciones


if condicion
    instrucciones
else
    otras instrucciones

#Operadores de comparacion
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

#Operadores lógicos
and 
or
!
not

"""

#Ejemplo 1

print("#### EJEMPLO 1 ###")

color = "rojo"
if color == "rojo":
    print("El color es Rojo")
else:
    print("Color incorrecto")

#EJEMPLO 2
print("### EJEMPLO 2 ###")

year = 2020
year = int(input("En qué año estamos? "))
if year >= 2021:
    print("Estamos de 2021 en adelante!!")
else:
    print("Es un año anterior a 2021")

#EJEMPLO 3
print("### EJEMPLO 3 ###")

nombre = input("Escribe tu nombre: ")
edad = int(input("¿Ingresa tu edad? "))
continente = input("¿De qué continente eres? ")
mayor_edad = 18


if edad >= mayor_edad:
    print(f"{nombre} es mayor de edad")
    
    if continente != "America":
        print("No eres americano")
    else:
        print(f"{nombre} es de América")

else:
    print(f"{nombre} no es mayor de edad y es de {continente}" )

#EJEMPLO 4
print("### EJEMPLO 4 ###")

dia = int(input("Introduce el número del día de la semana: "))
"""""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana")
"""""    

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")

#EJEMPLO 5
print("### EJEMPLO 5 ###")

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("Qué edad tienes? "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No está en edad de trabajar")

#EJEMPLO 6
print("### EJEMPLO 6 ###")

pais = "España"

if  not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un país de habla hispana")
else:
    print(f"{pais} SI es de habla hispana")

#EJEMPLO 7
print("### EJEMPLO 7 ###")

pais = "Alemania"

if  pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} NO es de habla hispana")

#EJEMPLO 8
print("### EJEMPLO 8 ###")

pais = "Alemania"

if  pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO un país de habla hispana")
else:
    print(f"{pais} SI es de habla hispana")