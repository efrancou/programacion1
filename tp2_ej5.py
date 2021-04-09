# EJ 5
# Resuelva el ejercicio 3 del TP1 aplicando el filtro para los CV.

# El área de RRHH de una empresa desea filtrar los CV de los postulantes para un puesto
# vacante, el requisito mínimo es la edad, pero en los datos solo tienen la fecha de
# nacimiento


postulante = int(input("Ingresa el año de nacimiento del postulante: "))
edad = (2020 - postulante)
edad_requerida = int(input("Ingrese la edad mínima: "))

if(edad >= edad_requerida):
    print("El postulante cumple con los requisitos")
else:
    print("El postulante no cumple los requisitos")

