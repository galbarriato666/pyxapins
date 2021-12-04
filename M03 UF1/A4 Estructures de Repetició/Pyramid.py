"""
Emmanuel Manzanilla García
08/11/2021
ASIXc1b M03 UF1

S'imprimeix una piràmide d'altura N de #

input

5



output

#

# #

# # #

# # # #

# # # # #

"""

mida = int(input("Introdueix mida: "))
for var1 in range(mida,0, -1):
    print("  "*var1 + "#" *(mida + 1 -var1 ))
