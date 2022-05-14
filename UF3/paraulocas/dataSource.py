
"""Umar Mohammad Riaz
04/05/2022
ASIXc 1B

This file gets the data from different sources"""


from crazyWords import *


def getDataFromKeyboard():  # Esta funcion recoge el texto por teclado.
    dades = input()
    return dades


def getDataFromFiles(inputFilePath):
    try:
        if os.path.isfile(inputFilePath) and os.path.exists(inputFilePath):
            with open(inputFilePath, "wt") as inp:
                for line in inp:
                    return line
    except Exception as e:
        log('equis')




