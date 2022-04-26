"""
UMAR MOHAMMAD RIAZ i EMMANUEL MANZANILLA GARCIA
09/03/2022
ASIXc 1B




Implementar en Python un programa que demani una frase per teclat i la retorni per pantalla amb les lletres de cada
paraula de la frase desordenada, tal i com diu l’estudi de la Universitat de Cambridge.
"""
import random


def getDataFromKeyboard():  # Esta funcion recoge el texto por teclado
    getDataFromKeyboard.text = input("")  # text = despues del punto, nombre de la variable 


def splitText():  # Funcion que separa en una lista 2D cada palabra y letra
    splitText.text = []  # funcion + .text "otra variable llamada text de la funcion actual"
    text = getDataFromKeyboard.text  # asigna variable llamando a funcion gtdfk
    listWordsText = text.split()  # Separa las palabras y la mete en lista llamada listwordtext
    for paraula in listWordsText:  # Separa las letras recorre cada palabra
        splitText.text.append(list(
            paraula))  # cada palabra la separa en letras y la mete en una lista  nueva. Llamas la variable splittext y vamos añadiendo (append) cada letra con la funcion list(paraula) La funcion list separa en letras

        # de paraula creamos una lista (list) la cual vamos appendeando en split.text que estaba vacia


def mixWords():  # Esta función mezcla el texto separado
    mixWords.mixed = []  # lista vacia .mixed es el nombre (variable global)
    text = splitText.text  # aqui llamamos al texto separado que hemos hecho en la ultima linea de la anterior funcion
    mixedWord = []  # variable temporal
    cont = 0  # contador
    for word in range(len(text)):  # en la longitud de este texto, que son las palabras separadas
        wordSize = len(text[cont])  # guardar la longitud de cada palabra
        if wordSize != 1:  # si la palabra no es uno
            startWord = list(text[cont][
                                 0])  # asignamos primera posicion a variable startword (convertimos la primera letra en una lista)
            endWord = list(text[cont][
                               -1])  # asignamos ultima posicion a variable endword (convertimos la ultima letra en lista tambien)
        else:
            startWord = list(text[cont][
                                 0])  # si es uno, solo coge un valor, para que al printar no duplique resultad (porque cumpliria la condicion de ser la ultima y la primera letra)
            endWord = list("")
        wordToShuffle = text[cont][1:-1]  # Guarda la palabra menos las posiciones 0 y -1
        # en el rango estamos poniendo desde donde hasta donde coge las letras, es decir, dejando fuera la posicion 0 y -1 (primera y ultima)

        random.shuffle(wordToShuffle)  # funcion que mezcla el contenido de la variable anterior wordToShuffle
        mixedWord.extend(
            startWord)  # le empezamos a decir que ponga las variables en la lista mixedword de manera ordenada, empieza aqui
        mixedWord.extend(wordToShuffle)  # sigue aqui, etc
        mixedWord.extend(endWord)  # same
        mixWords.mixed.append(mixedWord)  # haga un append de la palabra mixeada en la variable global
        mixedWord = []  # aqui vaciamos la variable temporal
        cont += 1  # cambiamos de palabra


def printText():  # Muestra por pantalla el texto mezclado
    for word in mixWords.mixed:  # por cada palabra en mixwords.mixed (1era dimension)  recorre la palabra
        for letter in word:  # por cada letra en word (letra, 2da dimension)
            print(letter, end="")  # va printando cada letra sin dejar espacio entre ellas end=""
        print(end=" ")  # hace un espacio por cada palabra


getDataFromKeyboard()
splitText()
mixWords()
printText()



