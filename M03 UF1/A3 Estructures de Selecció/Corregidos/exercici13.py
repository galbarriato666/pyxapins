"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Realitza un programa que demani per teclat tres nombres corresponents respectivament a un dia,
    mes i any i tot seguit indiqui si representen una data correcta.
"""

dia = int(input("Introdueix el dia:"))
mes = int(input("Introdueix el mes:"))
any = int(input("Introdueix l'any:"))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dies_del_mes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dies_del_mes = 30
elif mes == 2:
    if (any % 4 == 0 and not (any % 100 == 0)) or any % 400 == 0:
        dies_del_mes = 29
    else:
        dies_del_mes = 28
else:
    print("Data incorrecta")

if dia < 0 or dia > dies_del_mes:
    print("Data incorrecta")
else:
    print("Data correcta")
