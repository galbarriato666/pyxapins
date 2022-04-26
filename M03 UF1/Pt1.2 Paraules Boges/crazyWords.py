"""
This file splits and converts data into 'Paraules boges'
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
    cont = 0
    for word in range(len(text)):
        wordSize = len(text[cont])
        if wordSize > 3:
            startWord = list(text[cont][0])  # asignamos primera posicion a variable startword
            endWord = list(text[cont][-1])  # Asignamos ultima posicion a variable endword
            wordToShuffle = text[cont][1:-1]  # Guarda la palabra menos las posiciones 0 y -1
            random.shuffle(wordToShuffle)  # funcion que mezcla el contenido de la variable anterior wordToShuffle
            mixedWord.extend(startWord + wordToShuffle + endWord)
            mixedText.append(mixedWord)
        else:
            mixedText.append(list(text[cont]))
        mixedWord = []
        cont += 1

    return mixedText


def printText(mixedText):  # Muestra por pantalla el texto mezclado
    result = ""
    for word in mixedText:
        for letter in word:
            result += letter
        result += " "

    return result



def paraulesBoges():
    dades = getDataFromKeyboard()
    splitedText = splitText(dades)
    mixedText = mixWords(splitedText)
    resultat = printText(mixedText)
    return resultat
