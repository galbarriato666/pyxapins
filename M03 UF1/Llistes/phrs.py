'''Emmanuel Manzanilla García
01 / 02 /2022
ASIXc 1B M03 UF1 A5 - A5 + Pp3

Feu un programa que vagi llegint frases pel teclat i,
en acabar cada entrada d'una frase, mostri la frase encriptada.

Per encriptar la frase, ha de canviar les vocals per numeros del 1 al 5.

No fer diferències entre majúsucles i minúscules
ni lletras amb accents, totes s'han de tractar com si fossin minúscules i sense accent.'''

vocals = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
non_acc = {"á": "a", "à": "a", "é": "e", "è": "e", "í": "i", "ò": "o", "ó": "o", "ú": "u", "ù": "u"}

while True:
    frase = str(input("\n Introdueixi frase a encriptar: \n")).lower()
    for char in frase:
        if char in vocals:
            print(vocals[char], end="")
        else:
            print(char, end="")
    break
print("\n\n Fin del juego")