#Capturar excepciones y manejar errores en código
#suceptible a errores

"""
try:
    nombre= input("Cual es tu nombre: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, ingresa bien el nombre")

else:
    print("Todo funcionó correctamente")
finally:
    print("Fin de la iteración")
"""

#Manejar multiples excepciones
"""
try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: "+str(numero*numero))
except TypeError:
    print("Debes convertir tus cadadenas a enteros3")
#except ValueError:
#    print("Introduce un numero correcto")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error ", type(e).__name__)
"""

# Excepciones personalizadas 

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduzca la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) >=1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bievenido al master de Python {nombre} !!!")
except ValueError:
    print("Introduce los datos de manera correcta")
except Exception as e:
    print("Existe un error", e)