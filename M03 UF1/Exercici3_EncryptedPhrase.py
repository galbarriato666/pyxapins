"""
Emmanuel Manzanilla García
1r ASIXcB - A5 + Pp3 : Exercici3
01/02/2022

"""

lletres = {"a": "0", "b": "1", "c": "2", "d": "3",
           "e": "4", "f": "5", "g": "6", "h": "7",
           "i": "8", "j": "9", "k": "10", "l": "11",
           "m": "12", "n": "13", "o": "14", "p": "15",
           "q": "16", "r": "17", "s": "18", "t": "19",
           "u": "20", "v": "21", "w": "22", "x": "23",
           "y": "24", "z": "25"}


while True:
    phrase = str(input("Introdueix frase a encriptar: ")).lower()
    for word in phrase:
        if word in lletres:
            print(lletres[word],":",end="")
        else:
            print(word, end="")
    break
print("\n\n ***HACKEASTE EL PENTÁGONO***")
