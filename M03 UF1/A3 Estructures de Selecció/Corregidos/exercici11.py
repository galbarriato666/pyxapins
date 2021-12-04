"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Escriu un programa que llegeixi per pantalla la longitud dels tres costats d'un triangle. 
    El programa ha de ser capaç de determinar de quin tipus de triangle es tracta.

    Tingueu en compte que:
    - Si es compleix el teorema de Pitàgores, llavors és triangle rectangle
    - Si només dos costats del triangle són iguals llavors aquest és isòsceles
    - Si els tres costats són iguals llavors és un equilàter
    - Si no es compleix cap de les condicions anteriors, és un triangle escalè.
"""

costatA = float(input("Entra la longitud del costat A:"))
costatB = float(input("Entra la longitud del costat B:"))
costatC = float(input("Entra la longitud del costat C:"))

# Pitágoras
if costatA ** 2 + costatB ** 2 == costatC ** 2 or costatB ** 2 + costatC ** 2 == costatA ** 2 or costatC ** 2 + costatA ** 2 == costatB ** 2:
    print("Triangle Rectangle")
# Isòsceles
if (costatA == costatB and costatA != costatC) or (costatB == costatC and costatB != costatA) or (
        costatC == costatA and costatC != costatB):
    print("Triangle Isòsceles")
else:
    # Equilàter
    if costatA == costatB and costatA == costatC:
        print("Triangle Equilàter")
    else:
        print("Triangle Escalè")
