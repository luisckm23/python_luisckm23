"""
Hacer un programa que diga cuantos alumnos reprobaron y cuantos aprobaron

"""
alumno = 1
aprobados = 0
reprobados = 0

while alumno <= 5:
    calificacion = int(input("Ingrese la calificacion del alumno: "))
    alumno += 1
    if calificacion >=7:
        print(f"El alumno sacó {calificacion} está aprobado")
        aprobados +=1
    else:
        print(f"El alumno sacó {calificacion} está reprobado")
        reprobados += 1
print(f"La cantidad de aprobados es de {aprobados} y de reprobados es de {reprobados}")