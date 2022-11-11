total= 0
for i in range (0,5):
    numero= int(input("introduce un numero"))
    respuesta= input("quieres incluir este numero? (y/n")
    if respuesta=="y":
        total= total+numero
print (total)