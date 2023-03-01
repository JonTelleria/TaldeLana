import random 

def aimar():
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
        print("\nOso ongi!! kodea", 
        intentos, "intentotan asmatu duzu.\n")
        
def jonenJokoa():
   
    import random

    def tablerua(hitz_ezkutua, asmatutako_letra):
    
        print("Hitz sekretua: ", end="")
        for letra in hitz_ezkutua:
            if letra in asmatutako_letra:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        print()

    def sartuletra():
        
        letra = input("Sartu letra bat: ")
        return letra.lower()

    def jolastu():

        hitza = ["elefantea", "programazioa", "mendizalea", "klasea", "esternokleidomastoideo", "irakaslea"]
        hitz_ezkutua = random.choice(hitza)
        asmatutako_letra = set()
        sahiakerak = 6

        while sahiakerak > 0:
            tablerua(hitz_ezkutua, asmatutako_letra)
            letra = sartuletra()

            if letra in asmatutako_letra:
                print("letra hau sartuta dago sahiatu beste batekin")
                continue

            asmatutako_letra.add(letra)

            if letra in hitz_ezkutua:
                print("Oso ondo!!!letra hau hitz honetan dago!")
            else:
                sahiakerak -= 1
                print("Oooooohhh, letra hau ez dago hitz honetan. ", sahiakerak, "sahiakera gelditzen zaizkizu.")

            if set(hitz_ezkutua) == asmatutako_letra:
                print("IRABAZI DUZU")
                return

        print("oooooohhh galdu duzu. hitz eskutua:", hitz_ezkutua, "zen")

    jolastu()
 

       
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
    print("**   2.Ahorkatua                                      ** ")
    print("**   3.                                               ** ")
    print("**   0 para salir                                     ** ")
    print("**                                                    ** ")
    print("******************************************************** ")
    print("******************************************************** ")
 
    opcion = int(input("Aukeratu: "))
 
    if opcion == 1:
        juegoAimar = aimar()
    elif opcion == 2:
        
        juegoJon = jonenJokoa()
    elif opcion == 3:
        print("Opcion 3")
        break
    elif opcion == 0:
        break
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")

