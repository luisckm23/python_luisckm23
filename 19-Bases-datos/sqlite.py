#Importar el modulo
import sqlite3

#Conexión
conexion = sqlite3.connect('pruebas.db')

#Crear cursor
cursor = conexion.cursor()

#Crear TABLA
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"titulo  varchar(255), "+   
"descriptcion text, "+
"precio int(255) "+
")")

#Guardar cambios
conexion.commit()

"""
#Insertar DATOS
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripción del producto', 550)")
conexion.commit()
"""

#Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

#Insertar muchos registros de golpe
productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono portatil", "Buen Telefono", 140),
    ("Placa base", "Buena placa", 80),
    ("Tablet", "Buena tablet", 250),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

# Update/actualización
cursor.execute("UPDATE productos SET precio= 678 WHERE precio=80")

#Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 250; ")
productos = cursor.fetchall()

for producto in productos:
    print("ID:", producto[0])
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos; ")
producto = cursor.fetchone()
print(producto)

#Cerrar la conexion
conexion.close()