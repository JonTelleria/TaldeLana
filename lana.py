def jonenJokoa():
   
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
    
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
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Opcion 1")
        break
    elif opcion == 2:
        print ("Opcion 2")
        break
    elif opcion == 3:
        print("Opcion 3")
        break
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")