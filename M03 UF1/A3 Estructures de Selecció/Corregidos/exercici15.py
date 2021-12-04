"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    S'està organitzant un viatge d'estudis d'una escola, i s'ha de calcular quant ha de pagar 
    cada alumne i quant s'ha de pagar a la companyia de viatges pel servei.

    S'ha establert el següent:
    - si el nombre d'alumnes interessats en el viatge són 100 o més, cada alumne pagarà 65 euros
    - si el nombre d'alumnes interessats va de 50 a 99, se'ls cobrarà 70 euros
    - si són de 30 a 49 alumnes, es cobrarà 95 euros per alumne
    - i si són menys de 30, cada alumne pagarà el resultat de dividir el cost de l'autobús, 
    4.000 euros, entre el nombre d'alumnes interessats

    Escriu el programa que permeti determinar el pagament a la companyia d'autobusos i el que 
    ha de pagar cada alumne pel viatge.

    Nota: fixar-se que tan sols en l'últim cas l'import del cost de l’autobús és constant (4.000 euros),
    en la resta de casos variarà. 
"""
alumnes = int(input("Quants alumnes participan al viatge?:"))

if alumnes >= 100:
    cost_per_alumne = 65
if alumnes >= 50 and alumnes <= 99:
    cost_per_alumne = 70
if alumnes >= 30 and alumnes <= 49:
    cost_per_alumne = 95
if alumnes < 30 and alumnes > 0:
    cost_per_alumne = 4000 / alumnes
if alumnes > 0:
    cost_autobus = alumnes * cost_per_alumne
    print("El cost per alumne és %.2f euros." % cost_per_alumne)
    print("El cost de l'autobús és %.2f euros." % cost_autobus)
else:
    print("El nombre d'alumnes ha de ser un valor positiu.")
