"""
Emmanuel Manzanilla García
17/05/2022
ASIXb M03 Fonaments de Gestió de Fitxers - Prova Final
"""

import os
import datetime

outboundPath = os.getcwd()

def checkPath(vPath): #comprova el path (if exists)

    if os.path.exists(vPath) == True:
        return True
    else:
        return False

def WriteTreeFolder(output): #Elabora l'estructura de fitxers si no existeix abans

    for i in range(1, 4):
        if checkPath(os.path.join(output, f'D{i}')) == False:
            os.mkdir(os.path.join(output, f'D{i}'))
            if i == 1:
                for j in range(11, 14):
                    insideFolder = os.path.join(output, f'D{i}')
                    os.mkdir(os.path.join(insideFolder, f'D{j}'))
                    childPath = (os.path.join(insideFolder, f'D{j}'))
                    with open(os.path.join(childPath, "created.txt"), "wt", encoding='utf-8') as doc_exit:
                        doc_exit.write(f'{datetime.datetime.now()} - {os.path.abspath(f"D1/D{j}/created.txt")}')

            elif i == 2:
                for h in range(21, 23):
                    insideFolder = os.path.join(output, f'D{i}')
                    os.mkdir(os.path.join(insideFolder, f'D{h}'))
                    childPath = os.path.join(insideFolder, f'D{h}')
                    with open(os.path.join(childPath, "created.txt"), "wt", encoding='utf-8') as doc_exit:
                        doc_exit.write(f'{datetime.datetime.now()} - {os.path.abspath(f"D2/D{h}/created.txt")}')

            elif i == 3:
                insideFolder = os.path.join(output, f'D{i}')
                os.mkdir(os.path.join(insideFolder, f'D31'))
                childPath = os.path.join(insideFolder, f'D31')
                with open(os.path.join(childPath, "created.txt"), "wt", encoding='utf-8') as doc_exit:
                    doc_exit.write(f'{datetime.datetime.now()} - {os.path.abspath(f"D3/D31/created.txt")}')

WriteTreeFolder(outboundPath)
