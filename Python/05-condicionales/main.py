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

print("### Ejemplo 1 ###")

#color = input("Adivida cual es mi color favorito: ")
color = "rojo"

if color == "rojo":
    print("Enhorabuena ese es mi color favorito")
else:
    print("Ese no es mi color favorito")

#Ejemplo 2

print("\n### Ejemplo 2 ###")
#year = int(input("En qué año estamos: "))
year = 2010

if year >= 2021:
    print("Estamos de 2021 en adelante  ")
else:
    print("Es un año anterior a 2021")

#Ejemplo 3

print("\n### Ejemplo 3 ###")

nombre = "Luis"
ciudad = "Queretaro"
continente = "Europa"
edad = 14
mayoriaEdad = 21

if edad >= mayoriaEdad:
    print(f"{nombre} eres mayor de edad")

    if continente != "Europa":
        print("Eres europeo")
    else:
        print(f"No eres europeo, es de {ciudad}")
        
else:
    print(f"El usuario {nombre} no es mayor de edad porque tiene {edad} años")

    #Ejemplo 4

print("\n### Ejemplo 4 ###")

#dia = int(input("Introduce el numero de dia de la semana: "))
dia = 1
"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if  dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print ("Es viernes")
                else:
                    print("Es fin de semana")
"""
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


#Ejemplo 5

print("\n### Ejemplo 5 ###")

edadMinima = 18
edadMaxiama = 65
#edadOficial = int(input("Estás en edad de trabajar? "))
edadOficial = 14

if edadOficial >= 18 and edadOficial <= 65:
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")

#Ejemplo 6

print("\n### Ejemplo 6 ###")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"El pais {pais} es de habla hispana" )
else: 
    print(f"El pais {pais} no es de habla hispana ")

#Ejemplo 7

print("\n### Ejemplo 7 ###")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"El pais {pais} NO es de habla hispana" )
else: 
    print(f"El pais {pais} SÍ es de habla hispana ")

#Ejemplo 8

print("\n### Ejemplo 8 ###")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"El pais {pais} NO es de habla hispana" )
else: 
    print(f"El pais {pais} SÍ es de habla hispana ")