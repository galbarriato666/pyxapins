texto = "Hola. Que tal?, Como estamos? Contemos numeros: 13, 15, 19."  #crea una variable texto, para luego con la lista de signos, ver cuantos signos de puntu hay

signos_puntuacion = ["?", ".", ",", ":"] #aqui definimos la lista de signos de puntuación como tal

def contador_signos(texto, signos_puntuacion): #asocio las variables de antes con esta funcion, para usarlas dentro

    contador = 0 #inicializa en 0 como siempre con fors
    for letras in texto: #recorrido letra por letra en variable texto
        if letras in signos_puntuacion: #y si hay una coincidencia, sigue la proxima linea
            contador += 1 #que suma una al contador, porque queremos contar en esta funcion (contador signos jeje)

    return contador #muestra el resultado
def posicion_signos(texto, signos_puntuacion): #llamamos a las mismas variables en esta nueva funcion, donde sabremos posicion

    lista_signos = [] #creamos lista nueva
    for num_letras in range(len(texto)): #por i en range ( longitud ( variable texto )) el rango será la longitud de la variable texto introducida
        #esto basicamente cuenta cada caracter sea letra o signo en la variable texto
        for num_signos in range(len(signos_puntuacion)): #recorrido de los signos de puntuacion ya definidos en la variable de antes
            if texto[num_letras] == signos_puntuacion[num_signos] and signos_puntuacion[num_signos] not in lista_signos:
                #aqui ni puta idea de por qué ni como, nos lo creeremos
                lista_signos.append(signos_puntuacion[num_signos]) #aqui ni puta idea de por qué ni como, nos lo creeremos


    lista_lugar = [[] * 1 for i in range(len(lista_signos))] #bfff sin comentarios

    contador = 0
    for num_lista_signos in range(len(lista_signos)):
        for num_letras in range(len(texto)):
            if texto[num_letras] == lista_signos[num_lista_signos]:
                lista_lugar[contador].append(num_letras)
            if num_letras == len(texto) - 1:
                contador += 1
    return lista_signos, lista_lugar #calcula la posicion vete a saber como, nos lo creemos



def convertir_ACSII(texto,signos_puntuacion):  #funcion convertir a ascii
    for letras in texto:
        if letras == " ":
            list_ASCII.append(" ")
        elif letras in signos_puntuacion:
            numer_ASCII = ord(letras)
            list_ASCII.append(f'·{numer_ASCII}·')
        else:
            list_ASCII.append(letras)
    list_ASCII_string = ""

    for caracteres in list_ASCII:
        list_ASCII_string += str(caracteres)

    return list_ASCII_string

def menu():
    opciones = int(input("[0] Salir\n"
                         "[1] Contar signos puntuacion\n"
                         "[2] Lugar del un signo\n"
                         "[3] convertir signos en ACSI\n"
                         "¿Qué quieres hacer?: "))

    return opciones