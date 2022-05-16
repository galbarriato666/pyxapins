# Exercici 2

# Feu un programa anomenat ComptaParaulesFitxer que llegeixi un fitxer de text on hi ha tot de frases escrites en línies diferents.
# Per indicar el final del fitxer, hi ha una frase on només posa “fi”.
# Aquest programa ha de mostrar per pantalla el nombre de paraules que té cada frase, sense comptar la de “FI”.
# Les contraccions (l’, d’, etc.) compten com a part de la paraula associada.
#
# Per exemple, a partir d’aquest fitxer:
#
# Hi havia una vegada...
# Perquè ho ha fet avui?
# No està malament
# Si tu ho dius hi aniré
# Doncs d'acord
# FI
#
# La sortida per pantalla podria ser:
# La línia 1 té 4 paraules.
# La línia 2 té 5 paraules.eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
# La línia 3 té 3 paraules.
# La línia 4 té 6 paraules.
# La línia 5 té 2 paraules.


def filepath():
    filepath = './entrada/alvin.txt'
    return filepath


def ComptaParaulesFRASE(contar):
    """

    :param contar:
    :return:
    """
    palabras=contar.split()
    i=0
    while i < len(palabras):
        palabra = palabras[i]
        if palabra == 'FI':
            break
        i+=1
    print("Numero de palabras: ", i)


def readingFile(leer):
    with open(leer, 'rt', encoding='UTF-8') as reading:
        Compta


def main ():
    fichero = filepath()
    readingFile(fichero)
    ComptaParaulesFRASE(fichero)

main()