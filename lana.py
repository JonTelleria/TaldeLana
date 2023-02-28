import random 
import os
  


def aimar():
    import random

    # zenbaki onartuak jokoan
    zenbakiak = ('0','1','2','3','4','5','6','7','8','9')

    # igartzeko zenbaki randoma sortu
    zenbakiKop = 5
    kodea = ''

    i = 0

    while i < zenbakiKop:
        zenbRand = random.choice(zenbakiak)
        if not zenbRand in kodea:
            kodea += zenbRand
            i += 1    

    # iniciamos interaccion con el usuario
    print("\nOngi etorri Wordlen kopia polit batera!\n")
    print(zenbakiKop, "digitoko zenbakia igarri behar duzu")
    print("Ez baduzu nahi jarraitu idatzi 'fin'")
    saiakera = input("Zartu zure proposamena: ")

    #modo dios:
    #print(kodea)

    # "saiakera" "kodea"rekin komparatu, zuzenak eta kointzidentziak erakutzi
    intentos = 1
    while saiakera != kodea and saiakera != "fin":
        intentos = intentos + 1
        zuzenak = 0
        kointzidentziak = 0

        for i in range(zenbakiKop):
            if saiakera[i] == kodea[i]:
                zuzenak = zuzenak + 1
            elif saiakera[i] in kodea:
                kointzidentziak = kointzidentziak + 1
        print ("Zure saiakerak (", saiakera, ")", zuzenak,
            "zuzen eta ", kointzidentziak, "kointzidentzia dauka.")
        # urrengo saiakera
        saiakera = input("Saiatu berriro: ")

    if saiakera == "fin":
        print("kodea", kodea, " zen")
    else:
        print("Oso ongi!! kodea", 
        intentos, "intentotan asmatu duzu.")
    



    
i = 1
while i == 1:
    
    print("******************************************************** ")
    print("******************************************************** ")
    print("**                                                    ** ")
    print("**          |\\  /|  |||||   |\\    |  |     |          ** ")
    print("**          | \\/ |  |       | \\   |  |     |          ** ")
    print("**          |    |  ||||    |  \\  |  |     |          ** ")
    print("**          |    |  |       |   \\ |  |     |          ** ")
    print("**          |    |  |||||   |    \\|  |||||||          ** ")
    print("**                                                    ** ")
    print("**- - - - - - - - - - - - - - - - - - - - - - - - - - ** ")
    print("**   1.Wordlen kopia polit bat(Aimar)                 ** ")
    print("**   2.                                               ** ")
    print("**   3.                                               ** ")
    print("**   0 para salir                                     ** ")
    print("**                                                    ** ")
    print("******************************************************** ")
    print("******************************************************** ")
     
    print ("Elige una opcion")
 
    opcion = int(input("Aukeratu: "))
 
    if opcion == 1:
        juegoAimar = aimar()
    elif opcion == 2:
        print ("Opcion 2")
        break
    elif opcion == 3:
        print("Opcion 3")
        break
    elif opcion == 4:
        break
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")

