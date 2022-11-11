print(" cuadrado")
print(" triangulo")
print()
seleccion= int(input("introduce un numero"))
if seleccion== 1:
    lado= int(input("introduce la longitud de un lado"))
    area= lado*lado
    print("el area de tu forma seleccionada es", area)
elif seleccion== 2:
    base=int(input("introduce la longitud de la base"))
    altura= int(input("introduce la altura del triangulo"))
    area= (base*altura)/2
    print("el area de tu forma elegida es", area)
else:
    print("opcion incorrecta seleccionada")