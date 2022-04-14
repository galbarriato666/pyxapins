#condiciones y decisiones if y tal

titol = "Selector de móvil inteligente"
print(titol, "\n", "-" * len(titol), "\n")


sistema = input("Qué sistema te gusta más \n" "A: Android \n B: iOs").upper() 

if sistema == "A":
    dinero = input("Tienes tili dinero? S/N").upper()
    if dinero == "S":
        camara = input("Te importa la cámara del móvil? S/N ").upper()
        if camara == "S":
            print("Cómprate un Google Pixel SuperCam")
        elif camara == "N":
            print("Cómprate un android calidad precio")
        else: print("OPCION NO CONTEMPLADA")
    elif dinero == "N":
        print("Comprate un Android Chinardo")
    else: print("ERROR: Opcion no contemplada")

if sistema == "B":
    dinero = input("Tienes tili dinero? S/N").upper()
    if dinero == "S":
        print("Cómprate un iPhone Ultra Pro Max")
    elif dinero == "N":
        print("Iphone segunda mano jaja puto pobre xd")
    else: print("ERROR: Opcion no contemplada")