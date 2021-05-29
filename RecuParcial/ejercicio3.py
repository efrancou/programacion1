from random import randint

lista100 = []
lista001 = lista100

for i in range (0,100):
    numero = randint(0,100)
    lista100.append(numero)
print("La lista generada es:")
print(lista100)

lista100.sort()

print("Respuesta 3.A")
print("Rango de valores: ", lista100[0], lista100[99])
print("La diferencia entre el mayor y el menor es: ", lista100[0] - lista100[99])

print("Respuesta 3.B")
print(sum(lista100) / 100)

print ("Respuesta 3.C")
print("Lista en orden creciente: ", lista100)

lista001.sort(reverse=True)

print("Respuesta 3.D")
print("Lista en orden decreciente: ", lista001)

print("Respuesta 3.E")
for num in lista100:
    if(num % 3 > 0 and num % 2 > 0):
        print(num)