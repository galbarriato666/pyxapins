"""Exercici 20
Escriure un programa que a partir del nombre de monedes que tenim dels següents tipus: 2
€, 1 €, 50 cèntims, 20 cèntims i 10 cèntims, ens digui l'import corresponent en euros i
cèntims."""

ko = 100 

c1 = 1 * ko
c2 = 2 * ko
c50 = 50 % ko
c20 = 20 % ko
c10 = 10 % ko

print(c1+c2+c50+c20+c10)