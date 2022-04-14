from Funciones import * #from archivo Funcions importa *

def menu():
    opciones = int(input("[0] Salir\n"
                         "[1] Contar signos puntuacion\n"
                         "[2] Lugar del un signo\n"
                         "[3] convertir signos en ACSI\n"
                         "¿Qué quieres hacer?: "))

    return opciones
def muestra_resultados():
    opciones = menu()
    while opciones != 0:
        if opciones == 1:
            print(contador_signos(texto, signos_puntuacion))
            opciones = menu()
        elif opciones == 2:
            signos_lugar = posicion_signos(texto, signos_puntuacion)
            signos = signos_lugar[0]
            lugar = signos_lugar[1]
            for i in range(len(signos)):
                print(f'el signo: {signos[i]} se repite: {len(lugar[i])} y se encuentran en las posiciones: {lugar[i]}')

            opciones = menu()
        elif opciones == 3:
            print(convertir_ACSSI(texto,signos_puntuacion))
            opciones = menu()
        else:
            print("Opcion no registrada")
            opciones = menu()

    print("Adeu")


muestra_resultados()