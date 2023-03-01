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