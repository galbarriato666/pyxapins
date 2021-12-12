"""Exercici 15
S'està organitzant un viatge d'estudis d'una escola, i s'ha de calcular quant ha de pagar
cada alumne i quant s'ha de pagar a la companyia de viatges pel servei.
S'ha establert el següent:
- si el nombre d'alumnes interessats en el viatge són 100 o més, cada alumne pagarà
65 euros
- si el nombre d'alumnes interessats va de 50 a 99, se'ls cobrarà 70 euros
- si són de 30 a 49 alumnes, es cobrarà 95 euros per alumne
- i si són menys de 30, cada alumne pagarà el resultat de dividir el cost de l'autobús,
4.000 euros, entre el nombre d'alumnes interessats
Escriu el programa que permeti determinar el pagament a la companyia d'autobusos i el que
ha de pagar cada alumne pel viatge.
Nota: fixar-se que tan sols en l'últim cas l'import del cost de l’autobús és constant (4.000
euros), en la resta de casos variarà."""

numAlu = int(input("Num alumnes? "))

if numAlu >= 100:
    print("Cada un 65€, i en total", numAlu * 65)
elif numAlu >= 50 and numAlu <= 99:
    print("Cada un 70€, i en total", numAlu * 70)
elif numAlu > 29 and numAlu <= 49:
    print("Cada un 95€, i en total", numAlu * 95)
elif numAlu <= 29:
    print("Es divideix 4000 entre tots")
    numAlu = 4000 / numAlu
    print("Lo que es igual a", numAlu, "€")



