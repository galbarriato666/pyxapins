#menu va en el main o import from las funciones que necesite

def menu():
    opciones = -1
    while opciones != 0:
        opciones = int(input("[1] Tarea 1\n"
                             "[2] Tarea 2\n"
                             "[3] Tarea 3\n"
                             "[0] Salir\n"
                             "opcion: "))

        if opciones == 1:
            pass
        elif opciones == 2:
            pass
        elif opciones == 3:
            pass
        elif opciones == 0:
            pass
        else:
            ERROR = "Opcion no disponible"
            print(ERROR)

menu()