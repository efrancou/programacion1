# EJ 4
# Dada las tres notas obtenidas por un alumno en los distintos parciales, determinar si el
# mismo está aprobado o desaprobado.

aprobado = 6
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

if((nota1 + nota2 + nota3)/3 >= aprobado):
    print("El alumno aprobó")
else:
    print("El alumno desaprobo")
