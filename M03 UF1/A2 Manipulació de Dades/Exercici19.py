"""Exercici 19
Implementa el programa que calculi la nota d'un test realitzat per un estudiant.
La nota es calcularà així: per cada resposta correcta se sumaran cinc punts, per cada
incorrecta es restarà un punt i les respostes en blanc ni sumaran ni restaran. El programa
demanarà les dades estrictament necessàries i mostrarà en pantalla la nota del test"""


correct = int(input("Entra el número de respostes correctes:"))
incorrect = int(input("Entra el número de respostes incorrectes:"))
nota = correct * 5 + incorrect * (-1) # primero multiplica los valores correctos * 5, que es lo que pide, luego hace lo mismo 
# * (-1) (asi se hace, no se pq)
print("Nota del test:", nota)