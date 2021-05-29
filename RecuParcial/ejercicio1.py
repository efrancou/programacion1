personaje1 = input("Ingrese el nombre del primer personaje ")
personaje2 = input("Ingrese el nombre del segundo personaje ")

alturap1 = int(input("Ingrese la altura del primer personaje "))
alturap2 = int(input("Ingrese la altura del segundo personaje " ))

pesop1 = int(input("Ingrese el peso del primer personaje "))
pesop2 = int(input("Ingrese el peso del segundo personaje " ))

origenp1 = input("Ingrese el origen del primer personaje ")
origenp2 = input("Ingrese el origen del segundo personaje ")

pelisp1 = int(input("Ingrese la cantidad de pelis del primer personaje "))
pelisp2 = int(input("Ingrese la cantidad de pelis del segundo personaje "))

pers1 = [personaje1, alturap1, origenp1, pelisp1, pesop1]
pers2 = [personaje2, alturap2, origenp2, pelisp2, pesop2]

print("Respuesta 1.A")

if (pers1[1] > pers2[1]):
    print(pers1[0], "es mas alto")
elif (pers1[1] == pers2[1]):
    print("Ambos pesan lo mismo che")
else:
    print(pers2[0], "es más alto")

print("Respuesta 1.B")

if (pers1[4] > pers2[4]):
    print(pers1[0], "es más pesado")
elif (pers1[4] == pers2[4]):
    print("Pesan lo mismo")
else:
    print(pers2[0], "es más pesado")

print("Respuesta 1.C")

if (pers1[4] > pers2[3]):
    print(pers1[0], "participo en mas pelis")
elif (pers1[3] == pers2[3]):
    print("Participaron en la misma cantidad de pelis")
else:
    print(pers2[0], "participo en mas pelis")

print("Respuesta 1.D")

if(personaje1.capitalize() == "Yoda" or personaje1.capitalize() == "Chewbacca" or personaje2.capitalize()== "Yoda" or personaje2.capitalize() == "Chewbacca"):
    print("Uno de los personajes se llama Yoda o Chew")
else:
    print("Ninguno de los personajes se llama Yoda o Chew")
