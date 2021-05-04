"""

Variables locales: se definen dentro de la función 
y no se pueden usar fuera de ella, solo están dispomibles dentro de ella
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de las funciones y 
están disponibles dentro y fuera de ella.

"""

#Varibles globales

frase = "Ni los genios son tan genios, ni los mediocres tan mediocres" #variiable global
print(frase)

def hola_mundo():
    frase = "Hola mundo"
    print("Dentro de la función")
    print(frase)

    year = 2012
    print(year) #variable local

    global website #variable local hecha global
    website = "www.cotorreo.com"  #variable local hecha global
    print("Dentro", website)

    return "Dato devuelto " + str(year)

print(hola_mundo())
print("Fuera ", website) #aquí se imprime la variable local hecha global