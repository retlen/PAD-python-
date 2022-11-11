direccion= input("quieres contar hacia arriba o hacia abajo? ar/ab")
if direccion=="u":
    numero= int(input("cual es el numero de hasta arriba"))
    for i in range (1,numero+1):
        print(i)
elif direccion=="d":
    num=int(input("introduce un numero menor a 20"))
for i in range (20,numero-1, -1):
        print(i)
else:
    print("no lo entiendo")