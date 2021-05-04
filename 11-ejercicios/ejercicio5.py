"""
Crear una lista con el contenido de esta tabla
ACCION  AVENTURA    DEPORTES
GTA     ASASSINS    FIFA21 
COD     CRASH       PRO21
PUG     PRINCE      MOTO GP

Mostrar la informacion ordenada
"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "COD", "PUG"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASASSINS", "CRASH", "PRINCE"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA21", "PRO21", "MOTO GP"]
    }
]

for categoria in tabla:
    print(f"----------{categoria['categoria']}-----------")
    for juego in categoria['juegos']:
        print(juego)