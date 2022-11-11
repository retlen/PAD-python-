import math
radio=int(input("introduzca radio:"))
profundidad=int(input("introduzca profundidad:"))
area=math.pi*(radio**2)
volumen=area*profundidad
print(round(volumen,3))