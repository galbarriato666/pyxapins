def readFile(leer):
    with open(leer, 'rt', encoding='UTF-8') as reading:
        print(reading.readline()) or readlines #lo pone en lista

def readFile(leer):

    with open(leer, 'rt', encoding='UTF-8') as reading:
       for frase in reading:
           print(frase)  #esta es otra manera de recorrer/printar.