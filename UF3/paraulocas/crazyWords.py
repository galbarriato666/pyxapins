"""
Umar Mohammad Riaz
04/05/2022
ASIXc 1B

This file splits and converts data into 'Paraules boges'
"""

from datetime import date, datetime
from time import sleep

from dataSource import *
import random
import os

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



def paraulesBoges():
    dades = getDataFromKeyboard()
    splitedText = splitText(dades)
    mixedText = mixWords(splitedText)
    resultat = printText(mixedText)
    return resultat


def currentDateTime():
    now = datetime.now()
    currentDateTime = now.strftime("%d/%m/%Y %H:%M:%S:%f")[:-3]
    return currentDateTime


def log(message):
    if not os.path.exists("log"):
        os.mkdir("log")
    with open("log/error.log", "a") as log:
        log.write(f"{currentDateTime()} - {message}\n")



def personalizedException(exception):
    file = __file__
    file = os.path.split(file)
    filename = file[1]
    error = f"{type(exception).__name__} at line {exception.__traceback__.tb_lineno} of {filename}: {exception}"
    return error
