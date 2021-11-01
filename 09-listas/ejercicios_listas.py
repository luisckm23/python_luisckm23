#Escribir un programa que almacede las asignaturas de un curso
#Ejemplo: Matemáticas, Física, Química, Historia, Lengua

listaMaterias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(listaMaterias[:])

"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
"""
listaMaterias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for materias in listaMaterias:
    print(f"Yo estudio la asinatura de: {materias} ")

"""
Escribir un programa que almacene las asignaturas de un curso en una lista, pregunte al usuario la nota que ha sacado en cada una, 
después las muestre por pantalla con el mensaje 'En <asignatura> has sacado <nota> donde <asignatura> es cada una de las
asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
calificacion = []

for mat in materias:
    calif = input("Qué nota sacaste en " + mat + "? " )
    calificacion.append(calif)

for i in range(len(materias)):
    print("En " + materias[i] + "has sacado " + calificacion[i])