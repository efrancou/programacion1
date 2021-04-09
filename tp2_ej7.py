# EJ 7
# Dado el monto de la compra de un cliente y la tarjeta de crédito con la que paga
# determinar el monto final de la compra considerando los siguientes criterios:
# a. Si la tarjeta es Visa se debe aplicar un recargo del 7 %
# b. Si la tarjeta es Mastercard se le aplica un recargo del 11%


compra = float(input("Ingrese el monto de la compra: "))
tarjeta = str(input("Ingrese la tarjeta: "))
visa = 1.07
master = 1.11

if(tarjeta == "visa"):
    print("El total seria: ", (compra * visa))
else:
    print("El total seria: ", (compra * master))