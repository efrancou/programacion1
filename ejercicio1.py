# EJERCICIO 1

"""
base = int(input("Ingrese el valor de la base"))
altura = int(input("Ingrese la altura"))

#ACA SE ALMACENA EN UNA VARIABLE PARA PODER REUTILIZAR EL DATO.
area = base * altura
print("El area del rectangulo es:", area, "cm")
#CUANDO ES UN SCRIPT CHIQUITO, NO ES NECESARIO MANTENERLO EN MEMORIA.
print("El area del rectangulo es", base * altura, "cm")
"""

# EJERCICIO 2


"""
preciodol = input("Ingrese el valor en dólares de la máquina:" )
precio = float(preciodol)
cotizaciondol = input("Ingrese la cotización del dolar:" )
valor_dolar = float(cotizaciondol)
print ("El precio en pesos es:", precio * valor_dolar, "ARS")
"""

"""
valor_producto = float(input("Ingrese el valor en dólares: "))
valor_dolar = float(input("Ingrese la cotización del dolar: "))
print("El valor en PESOS es: ", valor_producto * valor_dolar, "ARS")
"""

# EJERCICIO 3

"""
ano_nacimiento = int(input("Ingrese el año de nacimiento del postulante: "))
ano_actual = int(input("Ingrese el año actual: "))

print("La edad del postulante es: ", ano_actual - ano_nacimiento, "años")
"""

# EJERCICIO 4

"""
base_triangulo = float(input("Ingrese la base del triangulo: "))
alt_triangulo = float(input("Ingrese la altura del triagulo: "))

print("El área del triangulo es: ", (base_triangulo * alt_triangulo) / 2 )
"""

# EJERCICIO 5


"""
precio_hora = float(input("Ingrese el precio por hora: "))
cantidad_horas = int(input("Ingrese la cantidad de horas: "))

print("Su total es: ", precio_hora * cantidad_horas, "ARS")
"""

"""
precio_hora = 500
cantidad_horas = int(input("Ingrese la cantidad de horas: "))

print("Su total es: ", precio_hora * cantidad_horas, "ARS")
"""

# EJERCICIO 6

# Una pinturería debe elaborar el presupuesto para un cliente y necesita calcular el costo
# total, este se deriva de la cantidad de pintura requerida y de la mano de obra, teniendo en
# cuenta lo siguiente: se requiere un litro de pintura por m2 y el costo de mano de obra es
# del 45 % del precio total de pintura.

"""
cantidad_m2 = int(input("Ingrese la cantidad de metros cuadrados: "))
precio_pintura = int(input("Ingrese el precio de la pintura: "))

print("El presupuesto sería: ", (cantidad_m2 * precio_pintura) + (cantidad_m2 * precio_pintura * 0.45), "ARS")
"""


#EJERCICIO 7

#Se desea calcular cuántos metros se deben recorreré para atravesar una plaza en diagonal,
#pero solo se conocen las distancia de las cuadras de ambos lados.
"""
from math import sqrt

lado1 = int(input("Ingrese el valor del lado 1: "))
lado2 = int(input("Ingrese el valor del lado 2: "))

diagonal = (round(sqrt(lado1 ** 2 + lado2 ** 2),2))
print(diagonal)
"""

#EJERCICIO 8

# El entrenador de un equipo de básquet desea determinar la eficiencia en tiros de campo
# de un jugador "X".

"""
cant_tiros = int(input("Ingrese la cantidad de tiros: "))
cant_aciertos = int(input("Ingrese la cantidad de aciertos: "))

print("La eficiencia es del: ", cant_aciertos * 100 / cant_tiros, "%")
"""


#EJERCICIO 9

#Una empresa de transportes les cobra a sus pasajeros por kilómetros recorridos, y
#necesita poder calcular el monto a cobrar a un cliente cuando se baja.

"""
kilom_rec = int(input("Ingrese la cantidad de Kilometros recorrdos: "))
x_kilom = float(input("Ingrese el valor por kilometro: "))

print(kilom_rec * x_kilom)
"""

#EJERCICIO 10

#Determinar cuánto demora una persona en ir en bicicleta de un lugar a otros, suponiendo
#que esta se mueve a una velocidad constante y se conocen la cantidad de kilómetros del
#camino.

"""
print("La bicicleta se mueve a 5KM/h")
velocidad = 5
cant_kilom = int(input("Ingrese la cantidad de kilometros a recorrer: "))

print("La bicicleta tardará", round(cant_kilom / velocidad), "horas")
"""

#EJERCICIO 11

#Una empresa telefónica debe facturar el costo de las llamadas telefónicas a sus cliente
#para esto les cobra por tiempo de llamada (por minuto) pero además le adiciona un 0,5 %
#del monto total de la llamada.

"""
precio_minuto = float(input("Ingrese el precio por minuto: "))
cant_minutos = int(input("Ingrese la cantidad de minutos: "))

print("El costo total es: ", round((precio_minuto * cant_minutos) * 1.005,1))
"""


#EJERCICIO 12

#Una empresa distribuidora de energía le cobrar a sus abonados el consumo de kW por
#hora, pero además debe sumarle el 0,21 % de impuesto, pero actualmente todos los
#cliente están dentro de un plan de promoción que les descuenta el 3,7 % del monto total a
#pagar.
"""
precio_kw = 10
consumo = int(input("Ingrese la cantidad de Kw consumidos: "))

print("El costo total es: ", round(((precio_kw * consumo) * 1.0021) / 1.037,2))
"""

#EJERCICIO 13

#Un supermercado está estableciendo el precio de venta para nuevos productos, de estos
#productos desean generar el 27 % de ganancia.

"""
costo = float(input("Ingrese precio de costo del producto: "))
multiplicador_precio_ganancia = 1.27
print("El precio de venta del producto es: $", (costo * multiplicador_precio_ganancia))
"""

#EJERCICIO 14

#Un profesor desea calcular el promedio de un alumno a lo largo de los cuatro parciales que
#rindió.

"""
parcial1 = float(input("Ingrese la nota del Parcial 1:"))
parcial2 = float(input("Ingrese la nota del Parcial 2: "))
parcial3 = float(input("Ingrese la nota del Parcial 3: "))
parcial4 = float(input("Ingrese la nota del Parcial 4: "))

print("El promedio es: ", (parcial1 + parcial2 + parcial3 + parcial4) / 4)
"""

#EJERCICIO 15

#Un grupo de amigos se hospedan en un hotel, y al momento de pagar se dividen los gastos
#de la siguiente manera:
#a. Iván paga el 40 %
#b. German paga el 33 %
#c. Esteban paga el 55 % de lo que pago Iván
#d. Hernán paga el resto
#Determinar cuánto debe pagar cada uno.

"""
gastos_hotel = float(input("Ingrese el total gastado en el hotel: "))
ivan = 0.4
german = 0.33
esteban = (ivan * 0.55)
hernan = (1 - ivan - german - esteban)

print("Ivan tendrá que pagar: $", (gastos_hotel * ivan))
print("German tendrá que pagar: $", (gastos_hotel * german))
print("Esteban tendrá que pagar: $", round((gastos_hotel * esteban),2))
print("Hernan tendrá que pagar: $", round((gastos_hotel * hernan)))
"""

#EJERCICIO 16

#Calcular el promedio de temperatura y presión recolectado por una estación
#meteorológica en una semana, considerando que realiza solo una medición al día.

"""
temp_dia_uno = float(input("Ingrese la temperatura del Domingo: "))
presion_dia_uno = float(input("Ingrese la presión del Domingo: "))
temp_dia_dos = float(input("Ingrese la temperatura del Lunes: "))
presion_dia_dos = float(input("Ingrese la presión del Lunes: "))
temp_dia_tres = float(input("Ingrese la temperatura del Martes: "))
presion_dia_tres = float(input("Ingrese la presión del Martes: "))
temp_dia_cuatro = float(input("Ingrese la temperatura del Miercoles: "))
presion_dia_cuatro = float(input("Ingrese la presión del Miercoles: "))
temp_dia_cinco = float(input("Ingrese la temperatura del Jueves: "))
presion_dia_cinco = float(input("Ingrese la presión del Jueves: "))
temp_dia_seis = float(input("Ingrese la temperatura del Viernes: "))
presion_dia_seis = float(input("Ingrese la presión del Viernes: "))
temp_dia_siete = float(input("Ingrese la temperatura del Sabado: "))
presion_dia_siete = float(input("Ingrese la presión del Sabado: "))

print("El promedio de temperatura es: ", (temp_dia_uno + temp_dia_dos + temp_dia_tres + temp_dia_cuatro + temp_dia_cinco + temp_dia_seis + temp_dia_siete) / 7)
print("El promedio de temperatura es: ", (presion_dia_uno + presion_dia_dos + presion_dia_tres + presion_dia_cuatro + presion_dia_cinco + presion_dia_seis + presion_dia_siete) / 7)
"""

#EJERCICIO 17

#Convertir un valor entero de horas a segundos.

horas = int(input("Ingrese la cantidad de horas: "))

print(horas, "horas equivalen a: ", ((horas*60)*60), "segundos")