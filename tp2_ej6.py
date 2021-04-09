# EJ 6
# Dado dos números determinar cuál es el mayor o si son iguales.


numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if(numero1 == numero2):
    print("Ambos numeros son iguales")
else:
    if(numero1 < numero2):
        print("El primer número es menor que el segundo")
    else:
        print("El primer número es mayor que el segundo")
