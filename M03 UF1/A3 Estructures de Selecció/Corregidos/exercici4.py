"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Escriu un programa que demani dos nombres per teclat i mostri la seva divisió. El programa ha de comprovar si el 
    segon nombre és igual a zero. Si ho és en lloc de realitzar i mostrar el resultat de la divisió ha de mostrar un
    missatge d'error per pantalla indicant que la divisió no es pot realitzar, ja que el segon nombre és zero.
"""
dividend = int(input('Entra el primer nombre:'));
divisor = int(input('Entra el segon nombre:'));
if divisor == 0:
    print('No pots dividir per 0')
else:
    print('La divisió és %f' % (dividend / divisor))
