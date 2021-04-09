# CONDICIONAL SIMPLE - TIENE UNA SOLA RAMA.
"""
numero = int(input ("Ingrese un número: "))
if(numero < 19):
    print("El numero es menor que 19")
print("fin del algoritmo")
"""

# CONDICIONAL COMPUESTO

"""
numero = int("Ingrese un numero: ")
if(numero < 19):
    print("El numero es menor que 19")
else:
    print("El número es mayor")
"""

# EJ 2
# Determinar si un número dado es positivo o negativo.

"""
numero = int(input("Ingrese un número: "))

if(numero > 0):
    print("El número es positivo")
    if(numero == 0):
    print("El número es Cero")
else:
    print("El número es negativo")
"""

# EJ 3
# Determinar si un número dado es par o impar.
"""
numero = int(input("Ingrese un número"))

if(numero % 2 == 0):
    print("El numero es par")
else:
    print("El número es impar")
"""

# EJ 4
# Dada las tres notas obtenidas por un alumno en los distintos parciales, determinar si el
# mismo está aprobado o desaprobado.


"""
aprobado = 6
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

if((nota1 + nota2 + nota3)/3 >= aprobado):
    print("El alumno aprobó")
else:
    print("El alumno desaprobo")
"""

# EJ 5
# Resuelva el ejercicio 3 del TP1 aplicando el filtro para los CV.

# El área de RRHH de una empresa desea filtrar los CV de los postulantes para un puesto
# vacante, el requisito mínimo es la edad, pero en los datos solo tienen la fecha de
# nacimiento

"""
postulante = int(input("Ingresa el año de nacimiento del postulante: "))
edad = (2020 - postulante)
edad_requerida = int(input("Ingrese la edad mínima: "))

if(edad >= edad_requerida):
    print("El postulante cumple con los requisitos")
else:
    print("El postulante no cumple los requisitos")
"""

# EJ 6
# Dado dos números determinar cuál es el mayor o si son iguales.

"""
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if(numero1 == numero2):
    print("Ambos numeros son iguales")
else:
    if(numero1 < numero2):
        print("El primer número es menor que el segundo")
    else:
        print("El primer número es mayor que el segundo")
"""

# EJ 7
# Dado el monto de la compra de un cliente y la tarjeta de crédito con la que paga
# determinar el monto final de la compra considerando los siguientes criterios:
# a. Si la tarjeta es Visa se debe aplicar un recargo del 7 %
# b. Si la tarjeta es Mastercard se le aplica un recargo del 11%

"""
compra = float(input("Ingrese el monto de la compra: "))
tarjeta = str(input("Ingrese la tarjeta: "))
visa = 1.07
master = 1.11

if(tarjeta == "visa"):
    print("El total seria: ", (compra * visa))
else:
    print("El total seria: ", (compra * master))
"""

# EJ 8
# Ahora modifique el ejercicio anterior en el que además se conoce el número de cuotas en
# la que paga, y aplicar los siguientes criterios para obtener el monto final (los recargos por
# cuotas son los mismos para cualquier tarjeta):
# a. Si paga en una cuota no hay recargo por cuotas
# b. Si paga en tres cuotas el recargo es del 3 %
# c. Si paga en ocho el recargo es del 17 %
# d. Si paga en doce el recargo es del 32 %


monto = float(input("Ingrese el monto de la compra: "))
cuotas = int(input("Ingrese la cantidad de cuotas: "))
tarjeta = input("Ingrese la tarjeta: ")
recargo_visa = 1.07
recargo_master = 1.11

if(cuotas == 3):
    monto = monto * 1.03
elif(cuotas == 8):
    monto = monto * 1.17
elif(cuotas == 12):
    monto = monto * 1.32

if(tarjeta == "visa"):
    recargo_visa = monto * recargo_visa
    print("El monto total es: ", recargo_visa)
elif(tarjeta == "mastercard" ):
    recargo_master = monto * recargo_master
    print("El monto total es: ", recargo_master)


# EJ 9
# Dado el nombre, apellido y año de nacimiento de tres personas mostrar los datos de los
# que son mayores de edad.

"""
persona1_nombre = str(input("Ingrese el nombre de la persona: "))
persona1_ano = int(input("Ingrese el año de nacimiento: "))
persona2_nombre = str(input("Ingrese el nombre de la persona: "))
persona2_ano = int(input("Ingrese el año de nacimiento: "))
persona3_nombre = str(input("Ingrese el nombre de la persona: "))
persona3_ano = int(input("Ingrese el año de nacimiento: "))

if(persona1_ano >= 2002):
    print(persona1_nombre)
elif(persona2_ano >= 2002):
    print(persona2_nombre)
elif(persona3_ano >= 2002):
    print(persona3_nombre)
"""

# EJ 10

# EJ 11

# EJ 12