from logging import exception

#Funcion que te da la bienvenida
def bienvenida():
    print("Bienvenido a Recetoide")
    print("Las recetas estan en la ubicacion: ./Recetas")
    print("Hay 2 recetas de carne, ensalada, pastas y postre")
    print("")
    mostrar_menu()

#Muestra el menu y el usuario elige la opcion a realizar
def mostrar_menu():
    print("Estas son las opciones que tiene: ")
    print("0. Salir programa")
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoria")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")

    eleccion = input("¿Que opcion desea realizar?: ")
    llamada_metodos(eleccion)


def llamada_metodos(eleccion):
    if(eleccion == "0"):
        exit()

    elif(eleccion == "1"):
        leer_receta()

#-----------------------------------------------------------------------------------------------------------------------
##Métodos qeu realiza la funcionalidad

#Te lee un fichero entero y te lo muestra por pantalla
def leer_receta():
    #Le paso la ruta del fichero que quiere leer
    receta_a_leer = input("Indica la ruta de la receta a leer: ")

    #Abro el archivo --> r por que solo vamos a leerlo
    archivo = open(receta_a_leer, 'r')

    #El metodo .read() lee el archivo entero
    #Al meterlo en el print cuando lee el archivo lo imprime
    print("")
    print("Receta: ")
    print(archivo.read())

    #Cerramos el fichero
    archivo.close()

    #Trazas
    print("")
    print("Operacion exitosa")
    print("")
    mostrar_menu()

##https://ellibrodepython.com/

bienvenida()



