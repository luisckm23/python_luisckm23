"""
Crear un script que tenga cuatro variables, una lista, un string, un entero y un booleano
debe imprimir un mensaje según el tipo de dato de cada variable

"""

def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "String"
    elif tipo == int:
        result = "Entero"
    elif tipo == bool:
        result = "Booleano"
    
    return result




def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""

    if test:
       result = f"Este dato es del tipo: {traducirTipo(tipo)}"
    else:
        result = "No es correcto"
    
    return result


lista = ["HOLA MUNDO", 1]
titulo = "Master"
numero = 110
verdarero = True

print(comprobarTipado(lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdarero, bool))