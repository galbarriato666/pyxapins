"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Crea un programa el qual en funció dels punts x1, y1, x2, y2 corresponents al centre de dues 
    circumferències i els seus respectius radis r1 i r2, classifiqui aquestes circumferències com:
    - exteriors
    - tangents exteriors
    - assecants
    - tangents interiors
    - interiors
    - concèntriques

    Com és habitual les coordenades dels punts i els radis es demanaran a l'usuari per teclat. 
    La classificació de la relació entre les circumferències consistirà simplement en escriure un 
    missatge de pantalla. Per exemple, si les circumferències són tangents exteriors el programa 
    escriurà "Circumferències tangents exteriors".

    Nota: com ajuda a la implementació, es donen les següents definicions informals per classificar
    dues circumferències.

    - Circumferències exteriors: La distància entre els centres, d, és més gran que la suma dels radis.
    - Circumferències tangents exteriors: la distància entre els centres és igual a la suma dels radis.
    - Circumferències secants: La distància és menor que la suma dels radis i més gran que la seva diferència.
    - Circumferències tangents interiors: La distància entre els centres és igual a la diferència 
    entre els radis.
    - Circumferències interiors: La distància entre els centres és més gran que zero i menor que la 
    diferència entre els radis.
    - Circumferències concèntriques: La distància entre els centres és zero.
"""

import math

x1 = float(input("Entra la coordenada x del centre de la primera circunferencia:"))
y1 = float(input("Entra la coordenada y del centre de la primera circunferencia:"))
r1 = float(input("Entra el radi de la primera circunferencia:"))
x2 = float(input("Entra la coordenada x del centre de la segona circunferencia:"))
y2 = float(input("Entra la coordenada y del centre de la segona circunferencia:"))
r2 = float(input("Entra el radi de la segona circunferencia:"))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#  Circumferències exteriors
if distancia > (r1 + r2):
    print("Circumferències exteriors")
#  Circumferències tangents exteriors
if distancia == (r1 + r2):
    print("Circumferències tangents exteriors")
#  Circumferències secants
if distancia < (r1 + r2) and distancia > abs(r1 - r2):
    print("Circumferències secants")
#  Circumferències tangents interiors
if distancia == abs(r1 - r2):
    print("Circumferències tangents interiors")
#  Circumferències interiors
if distancia > 0 and distancia < abs(r1 - r2):
    print("Circumferències interiors")
#  Circumferències concèntriques
if distancia == 0:
    print("Circumferències concèntriques")