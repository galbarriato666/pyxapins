"""
Emmanuel Manzanilla García
26/10/2021
ASIXc1b M03 UF1

Exercici 18

Escriu un programa que donat un dia de la setmana (com a número, de l'1 a l'7), escrigui
el dia corresponent en lletres. Si introduïm un nombre que no sigui de l'1 a l'7, el programa mostrarà un missatge d'error.

Extra bonus: Modificar el programa per a tres idiomes: Anglès, Castellà i Català
"""
LANGUAGE = input("SELECT LANGUAGE \n English \n Castellano \n Català ")
if LANGUAGE == English:
    ENGLISHNUMBAH = int((input("Enter a number from 1 to 7 so I can guess the weekday "))
        if ENGLISHNUMBAH == 1:
            print("IT'S SUNDAY BRO")
        elif ENGLISHNUMBAH == 2:
            print ("IT'S MONDAY BRO")
        elif ENGLISHNUMBAH == 3:
            print("ITS TUESDAY BRO")
        elif ENGLISHNUMBAH == 4:
            print("ITS WEDNESDAY BRO")
        elif ENGLISHNUMBAH == 5:
            print("ITS THURSDAY BRO")
        elif ENGLISHNUMBAH == 6:
            print("ITS FRIDAY BRO")
        elif ENGLISHNUMBAH == 7:
            print("ITS SATURDAY BRO")








