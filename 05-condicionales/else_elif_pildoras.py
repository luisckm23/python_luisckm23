print("Calificaciones")

nota_alumno = int(input("Ingresa tu calificacion: "))

if nota_alumno < 5:
    print("Reprobado")

elif nota_alumno <= 6:
    print("Suficiente")

elif nota_alumno <= 7:
    print("Bien")

elif nota_alumno <= 9:
    print("Notable")

else:
    print("Sobresaliente")