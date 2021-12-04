"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Implementa un programa que donat un nombre enter entre un i dotze, imprimeixi el 
    nombre de dies que té el mes en qüestió.

    Com en exercicis anteriors, si el nombre introduït no està en el rang demanat, 
    es mostrarà un error.
"""

mes = int(input("Entra el nombre corresponent al mes (1-12):"))
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("31 dies")
elif mes == 2:
    print("28 o 29 dies")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("30 dies")
else:
    print("Mes incorrecte")
