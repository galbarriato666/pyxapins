"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Implementa el programa que calculi la nota d'un test realitzat per un estudiant.

    La nota es calcularà així: per cada resposta correcta se sumaran cinc punts, per cada incorrecta es restarà un punt
    i les respostes en blanc ni sumaran ni restaran. El programa demanarà les dades estrictament necessàries i mostrarà
    en pantalla la nota del test.
"""

correctes = int(input("Entra el número de respostes correctes:"))
incorrectes = int(input("Entra el número de respostes incorrectes:"))
nota = correctes * 5 + incorrectes * (-1)
print("Nota del test:", nota)
