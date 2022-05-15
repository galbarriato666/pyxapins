def ComptaParaulesFRASE(contar):
    """

    :param contar:
    :return:
    """
    palabras = contar.split()
    i = 0
    while i < len(palabras):
        palabra = palabras[i]
        if palabra == 'FI':
            break
        i += 1
    print("Numero de palabras: ", i)
