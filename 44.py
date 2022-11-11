num= int(input("a cuantos quieres invitar a la fiesta"))
if num < 10:
    for i in range (0,num):
        name= input("introduce un nombre")
        print(num,"ha sido invitado")
else:
    print("demasiada gente")