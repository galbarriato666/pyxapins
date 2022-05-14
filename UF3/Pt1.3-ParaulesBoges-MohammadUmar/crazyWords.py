"""
Umar Mohammad Riaz & Emmanuel Manzanilla
04/05/2022
ASIXc 1B

Crazy words functions
"""

from dataSource import *
import random

def splitText(dades):  # Funcion que separa en una lista 2D cada palabra y letra
    splitText.text = []
    listWordsText = dades.split()  # Separa las palabras
    splitedText = []
    for paraula in listWordsText:  # Separa las letras
        splitedText.append(list(paraula))

    return splitedText


def mixWords(splitedText):  # Esta función mezcla el texto separado
    mixedText = []
    text = splitedText
    mixedWord = []
    for word in range(len(text)):
        wordSize = len(text[word])
        if wordSize > 3:
            startWord = list(text[word][0])  # asignamos primera posicion a variable startword
            endWord = list(text[word][-1])  # Asignamos ultima posicion a variable endword
            wordToShuffle = text[word][1:-1]  # Guarda la palabra menos las posiciones 0 y -1
            random.shuffle(wordToShuffle)  # funcion que mezcla el contenido de la variable anterior wordToShuffle
            mixedWord.extend(startWord + wordToShuffle + endWord)
            mixedText.append(mixedWord)
        else:
            mixedText.append(list(text[word]))
        mixedWord = []

    return mixedText


def printText(mixedText):  # Muestra por pantalla el texto mezclado
    result = ""
    for word in mixedText:
        for letter in word:
            result += letter
        result += " "

    return result


def paraulesBoges(inputFolder):    # Calls all functions to make crazy words
    try:
        files = getFilesFromFolder(inputFolder)
        resultat = []
        cont = 0
        for filepath in files:
            mixedSingleText = []
            dades = getDataFromFile(filepath)
            cont += 1
            for linia in dades[0]:
                splitedText = splitText(linia)
                mixedText = mixWords(splitedText)
                resul = printText(mixedText)
                mixedSingleText.append(resul)
            resultat.append(mixedSingleText)
        writeOutput(resultat, files)
    except Exception as e:
        log(personalizedException(e))
