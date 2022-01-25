"""Donada una paraula i un valor indica quina lletra hi ha a la posició indicada

Els strings funcionen com si fossin llistes de chars

Input

Hello 1



Output

e
"""
entrada = input()
camps = entrada.spit(" ")
paraula = camps[0]

if camps[1].isnumeric():
    posicio = int(camps)
else:
    print("mirate las instrucciones")


#paraula = input()
#posicio = int(input())

if posicio <len(paraula) and posicio >= -len(paraula):
    print(paraula[posicio])
else:
    print("la has cagao")

