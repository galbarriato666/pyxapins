"""
Emmanuel Manzanilla García
05/10/2021
ASIXc1b M03 UF1

Exercici 3
Donats els catets a i b d'un triangle rectangle, escriure el codi Python que calcula
la seva hipotenusa. Recordar que la hipotenusa es calcula de la següent manera
(Teorema de Pitàgores):

c2 = a2 + b2 , on c és la hipotenusa. Per tant  c = √(a2 + b2)
"""
import math
Catet_A = float(input("catet A?" ))
Catet_B = float(input("catet B?" ))

#hipotenusa = math.sqrt(pow(Catet_A,2) + pow(Catet_B,2))

#otra manera de hacerlo es
#import math es lo primero puesto que vamos a utilizar las funciones matematicas.

#hipotenusa = math.sqrt(Catet_A**2 + Catet_B**2)
hipotenusa = (Catet_A**2 + Catet_B**2) ** 0.5  #ELEVADO A CERO COMA CINCO ES IGUAL QUE SQRT MUAHAHA

print("El resultat es " +str(hipotenusa))
