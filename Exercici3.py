"""
Emmanuel Manzanilla García
1r ASIXcB
19/01/2022

3. Programa de traducció d’insults. Crear un array de dues dimensions amb els insults en català i
afegir la traducció en castellà, anglès i klingon
El programa, demanarà a l’usuari que escrigui per teclat un insult i el mostrarà traduït a castellà,
anglès  i klingon.
"""

blasfemies = [["PELACANYES", "PELACAÑAS", "CANE PEELER", "DAB"],
              ["TANOCA", "TAN OCA", "SO GOOSE", "JERJXO"],
              ["PALLÚS", "ZOPENCO", "DUNCE", "JOR"],
              ["ABUSANANOS", "ABUSADOR DE NIÑOS", "PEDOPHILE", "OASTT"],
              ["LLEPACULS", "LAMECULOS", "ASS LICKER", "QES"],
              ["BANYUT", "CORNUDO", "CUCKOLD", "ENO"],
              ["XUPÒPTERE", "CHUPÓPTERO", "SUCKER", "OAO"],
              ["MITJA MERDA", "MEDIA MIERDA", "HALF A SHIT", "ALB ENE"],
              ["PYCHARMPINS", "MEAPINOS", "PINE PISSER", "JEJOS"],
              ["FIGAFLOR", "PUSILÀNIME", "FIG A FLOWER", "PEPI"]]




idiomes = ["CATALÀ", "CASTELLANO", "ENGLISH", "KLINGON"]
print("Idiomes: ", idiomes, "\n","Insults: ")
print("PELACANYES, TANOCA, PALLÚS, ABUSANANOS, LLEPACULS, BANYUT, XUPÒPTERE, MITJA MERDA, PYCHARMPINS, FIGAFLOR") #No he pogut fer la iteració automatica
print()
taco = input(str("Quin insult voldrà traduïr el senyoret avui?: \n"))
taco = taco.upper()

comptador = 0
notfound = True

while notfound and comptador != len(blasfemies):
    if taco.upper() in blasfemies[comptador]:
        for i, j in zip(idiomes, blasfemies[comptador]):
            print(i,": ", j)
            notfound = False
    else:
        comptador += 1

if notfound:
    print(f"\n '{taco}' no está en el diccionari!")
print()
print("End")
