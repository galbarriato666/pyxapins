 
x1 = int(input("x1: "))
y1 = int(input("y1 "))

x2 = int(input("x2: "))
y2 = int(input("y2: "))

r1 = int(input("r1: "))
r2 = int(input("r2: "))

#Circumferències exteriors: La distància entre els centres, d, és més gran que la suma dels radis.

d = ((x2 - x1) ** 2) + ((y2 + y1) ** 2) ** .5 
if d > (r1 + r2):
    print("Circunferencia exterior")
if d == (r1 + r2):
    print("Circum tangent")
if d < (r1 + r2) and d > abs(r1 - r2):
    print("Circum Secant")
if d == abs(r1 - r2):
    print("circum oaoaoa")
if d > 0 and d < abs(r1 - r2):
    print("circum aaa")
if d == 0:
    print("circum final")
print()

#cuando son tantas ecuaciones jodidas diferentes, no uso elif, uso if, por si las moscas. Con elif vas acorralando los valores