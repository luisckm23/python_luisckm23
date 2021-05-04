#import mimodulo
#from mimodulo import *

#print(holaMundo("Luis"))

#Modulo de fechas

import datetime

print(datetime.date.today())

fechaCompleta = datetime.datetime.now()
print(fechaCompleta)
print(fechaCompleta.year)
print(fechaCompleta.month)
print(fechaCompleta.day)

fechaPersonalizada = fechaCompleta.strftime("%d/%m/%Y %H:%M:%S")
print("Mi fecha personalizada es: ", fechaPersonalizada)

# Modulo de matematicas
import math 

print("Raíz cuadrada de diez", math.sqrt(10))
print("El numero Pi es:", float(math.pi))
print("Redondear  a la baja: ", math.floor(6.56798))
print("Redondear  al alza: ", math.ceil(6.56798))

# Modulo RANDOM

import random

print("Numero aleatorio entre 15 7y 67: ", random.randint(15, 67))