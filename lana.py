from os import system
import random


def aimar():
    opcion = str(input("Aukeratu: "))
    
    tablero()
    dado = random.randrange(1, 6)
    if dado == 1 or 2 or 3 or 4 or 6:
        print(dado)
        print("Urrengoan izango da!")
    elif dado == 5:
        print(dado)
        system("cls")
    
    
def tablero():
    print("_ _ _ _ _")
    print("|  ---  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  |_|  |")
    print("|  |_|  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  | |  |")
    print("|  ---  |")
    print("_ _ _ _ _")

    
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
    print("**   1.                                               ** ")
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

