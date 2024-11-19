import os.path
import shutil
from logging import exception
from os import listdir, mkdir


#Funcion que te da la bienvenida
def bienvenida():
    print("Bienvenido a Recetoide")
    print("Las recetas estan en la ubicacion: ./Recetas")
    print("Hay 2 recetas de carne, ensalada, pastas y postre")
    print("")
    mostrar_menu()

#Muestra el menu y el usuario elige la opcion a realizar
def mostrar_menu():
    print("")
    print("Estas son las opciones que tiene: ")
    print("0. Salir programa")
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoria")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")

    eleccion = input("¿Que opcion desea realizar?: ")
    print("")
    llamada_metodos(eleccion)


def llamada_metodos(eleccion):
    if(eleccion == "0"):
        exit() #Sale del programa

    elif(eleccion == "1"):
        leer_receta()

    elif(eleccion == "2"):
        crear_receta()

    elif(eleccion == "3"):
        crear_categoria()

    elif(eleccion == "4"):
        eliminar_receta()

    elif(eleccion == "5"):
        elimina_categoria()

#-----------------------------------------------------------------------------------------------------------------------
##Métodos que realizan la funcionalidad

#Te pide una carpeta, te lista el contenido esa carpeta, te pide un archivo de esa carpeta, lo lee entero y
# te muestra el contneido del archivo
def leer_receta():

    #Elijo que categoria (carpeta) tengo que leer
    categoria = input("Elige la categoria: ")

    #Saco una lista del contenido de esa carpeta  con el metodo listadir()
    ruta = "./Recetas/" +categoria
    print( listdir(ruta) )

    #Pregunto la receta que deseo leer
    receta = input("Elige la receta: ")

    #La leo y la imprimo
    file = open("./Recetas/"+categoria+"/"+receta, 'r')
    print("============================================================================================================")
    print(file.read())
    print("============================================================================================================")
    file.close()

    #Llamamos a mostrar menu para realizar otra operacion
    mostrar_menu()


#Creas un fichero pasandole tu la ruta (con el nuevo nombre incluido) y el contenido que va ha tener el fichero nuevo
def crear_receta():
    # Elijo que categoria (carpeta) tengo que leer
    categoria = input("Elige la categoria: ")

    ruta = "./Recetas/" + categoria

    # Pregunto la receta
    receta = input("Elige el nombre de la receta: ")

    #Pregunto el contenido de la receta
    contenido_receta = input("Escribe el contenido de la receta: ")

    #Concateno para tener la ruta completa
    ruta += "/"+receta

    #Abrimos un fichero en la ruta pasada de tipo w -> Borra el fichero con ese nombre si existe y crea uno con el nombre indicado
    fichero = open( ruta, 'w')

    #Escribo el contenido en el fichero
    fichero.write(contenido_receta)

    #Cierro el contenido del fichero
    fichero.close()
    print("Receta añadida con exito")
    print("")

    # Llamamos a mostrar menu para realizar otra operacion
    mostrar_menu()


#Te crea una carpeta si no existe, el nombre de la carpeta te lo pide por parametro
def crear_categoria():
    #Te pregunta el nombre de la carpeta
    nombre_carpeta = input("Que nombre va ha tener la nueva carpeta: ")

    #Creamos la ruta donde se va a crear la carpeta
    ruta = "./Recetas/"+nombre_carpeta

    if os.path.exists(ruta): #Si la ruta de la carpeta existe...
        print("La carpeta ya existe")
    else: #Si la ruta de la carpeta no existe...
        mkdir(ruta)
        print("Carpeta realizada con exito")

    # Llamamos a mostrar menu para realizar otra operacion
    mostrar_menu()


#Elimina SOLO UN ARCHIVO si existe
def eliminar_receta():
    # Elijo que categoria (carpeta) del archivo que quiero eliminar
    categoria = input("Elige la categoria: ")

    #Voy creando la ruta
    ruta = "./Recetas/" + categoria

    #Muestro al usuario lo que contiene esa carpeta
    print(listdir(ruta))

    # Pregunto la receta (archivo)
    receta = input("Elige el nombre de la receta: ")

    #Termino de concatenar la ruta
    ruta += "/" +receta

    if os.path.exists(ruta): #Si la ruta existe...
        os.remove(ruta) #Elimino el archivo
        print("Receta eliminada con existo")
    else: #Si la ruta no existe...
        print("La ruta pasada no existe")

    print("")

    # Llamamos a mostrar menu para realizar otra operacion
    mostrar_menu()


#Elimina una carpeta y el contenido de la carpeta
def elimina_categoria():
    # Elijo que categoria (carpeta) quiero eliminar
    categoria = input("Elige la categoria: ")

    ruta = "./Recetas/" +categoria

    if os.path.exists(ruta): #Si la ruta pasada existe
        shutil.rmtree(ruta) #Borra el contenido de la carpeta y la propia carpeta
        print("Carpeta y contenido eliminado con exito")
    else:
        print("La carpeta no existe")

    # Llamamos a mostrar menu para realizar otra operacion
    mostrar_menu()




bienvenida()