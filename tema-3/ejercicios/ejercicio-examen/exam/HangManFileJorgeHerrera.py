import os.path
import random


#ruta ./words.txt

#Pide una letra al usuario
def letra_usuario():
    return input("Dime una letra: ").lower()


#Devuelve la letra que vamos a elegir
def leer_fichero() -> str:
    ruta = input("Escribe la ruta del fichero a leer: ")

    contenido = "python\nguitar\nparagliding\ncomputer\nlibrary\nbeer"
    arrayContenido = ["python", "guitar", "paragliding", "computer","library", "beer"]

    if os.path.exists(ruta): #Si existe lo lee
        fichero = open(ruta, 'r')
        print( fichero.read() )
        fichero.close()
    else: #Si no existe se crea con el contenido
        fichero = open(ruta, 'w')
        fichero.write( contenido )
        fichero.close()

    #Elegimos la palabra
    palabra_elegida = arrayContenido[ random.randint(0, len(arrayContenido) -1) ]

    palabra_elegida = palabra_elegida.lower()

    return  palabra_elegida


#Juego del ahorcado
def ahorcado():

    #Consigo una palabra aleatoria
    palabra_a_adivinar = leer_fichero()

    #Vidas
    vidas = 6

    #La palabra que tengo que adivinar la divido en un array
    array_palabra_a_adivinar = list(palabra_a_adivinar)

    seguimiento_palabra = "_" * len(array_palabra_a_adivinar)

    while(vidas >0):
        print(f"Palabra: {seguimiento_palabra}")
        print(f"Vidas: {vidas}")
        letra_dicha_usuario = letra_usuario()

        if letra_dicha_usuario in array_palabra_a_adivinar:
            print("Has adivinado una letra! :)")

            nuevo_seguimiento = ""

            for i, letra in enumerate(palabra_a_adivinar):
                if letra == letra_dicha_usuario or seguimiento_palabra[i] != "_":
                    nuevo_seguimiento += letra
                else:
                    nuevo_seguimiento += "_"
            seguimiento_palabra = nuevo_seguimiento
        else:
            vidas -= 1
            print("No has adivinado la letra :(")

        if "_" not in seguimiento_palabra:
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_a_adivinar}")
            break
        else:
            print(f"Has perdido. La palabra era: {palabra_a_adivinar}")










ahorcado()