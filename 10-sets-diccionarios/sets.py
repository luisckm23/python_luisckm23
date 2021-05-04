"""
Set es un tipo de datos para tener una coleccion de valores, sin indice ni orden

"""

personas = {
    "Victor", 
    "Manuel",
    "Francisco"
}

personas.add("Paco")
personas.remove("Francisco")
print(type(personas))
print(personas)