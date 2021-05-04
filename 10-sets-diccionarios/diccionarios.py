"""
Diccionarios tipo de dato que almacena datos en formato clave-valor

"""

persona = {
    "nombre" : "Victor",
    "apellidos ": "Robles",
    "web": "victorrobles.web"
}

print(persona["web"])


# Lista con diccionarios

contactos = [
    {
        'nombre' : 'antonio',
        'email': 'anotnio@gmail.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'salvador',
        'email': 'salvador.com'
    }
]

print(contactos[0]['nombre'])

print("\nListado de nombres")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("---------------------------------------------")