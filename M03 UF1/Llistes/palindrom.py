"""Indica si una paraula és palíndrom.



Exemples de palíndroms:

cec, cuc, gag, mínim, nan, nen, pipiripip…"""




palin = input("És palindrom? ").upper()
palin2 = palin[::-1]

if palin == palin2:
    print("IT'S CAPICUA!")
else:
    print("NOT CAPICUA!")
