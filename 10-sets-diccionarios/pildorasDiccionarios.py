miDiccionario = {"Alemania": "Berlin", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"} #Van entre llave
miDiccionario["Italia"]="Lisboa" #Añade un nuevo elemento
print(miDiccionario)
miDiccionario["Italia"]="Roma" #Corregir un valor
print(miDiccionario)
del miDiccionario["Reino Unido"] #Borra una Clave:Valor
print(miDiccionario)

miDiccionario2={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3} #Se pueden generar diccionarios alfanuméricos
print(miDiccionario2)

#Genera una tupla y a cada Cavle su Valor con el índice correspondiente
miTupla=["España", "Francia", "Alemania", "Reino Unido"]
miDiccionario3 = {miTupla[0]:"Madrid", miTupla[1]:"París", miTupla[2]:"Londres", miTupla[3]:"Berlín"}
print(miDiccionario3["Francia"])

#Combina un diccionario con una tupla
miDiccionario4 ={23:"Jordan", "Nombre": "Michael", "Equipo":"Chicago", "Anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(miDiccionario4["Anillos"])

#Guardar un diccionario dentro de otro diccionario
miDiccionario5 ={23:"Jordan", "Nombre": "Michael", "Equipo":"Chicago", "Anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(miDiccionario5)
print(miDiccionario5.keys()) #Nos da las Claves del diccionario
print(miDiccionario5.values()) #Nos da los Valores del diccionario
print(len(miDiccionario5)) #Nos da la longitud del diccionario en Clave:Valor