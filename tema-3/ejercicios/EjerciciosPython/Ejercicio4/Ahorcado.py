import random

def letra_usuario():
    return input("Dime una letra: ").lower()


def ahorcado():

    #Vidas
    vidas = 6

    #Palabras a elegir
    array_palabras = ["java", "python", "windows"]

    #Guardamos la palabra elegida
    palabra_elegida = array_palabras[ random.randint(0, len(array_palabras) -1) ]
    palabra_elegida = palabra_elegida.lower()

    #Escribimos _ por cada letra de la palabra
    seguimiento_palabra = "_" * len(palabra_elegida)
    letras_adivinadas = []

    #Mientras que tengamos vidas
    while (vidas > 0):
        print(f"Palabra: {seguimiento_palabra}")
        print(f"Vidas restantes: {vidas}")
        letra_dicha_usuario = letra_usuario()

        #Comprobamos si la letra del usuario está en nuestra palabra
        if letra_dicha_usuario in palabra_elegida:
            print("Has adivinado una letra! :)")

            #Mostramos el seguimiento de la palabra
            nuevo_seguimiento = ""

            #Enumerate es para iterar sobre cada letra que haya en palabra_elegida
            for i, letra in enumerate(palabra_elegida):
                if letra == letra_dicha_usuario or seguimiento_palabra[i] != "_" :
                    nuevo_seguimiento += letra
                else:
                    nuevo_seguimiento += "_"

            seguimiento_palabra = nuevo_seguimiento
        else:
            vidas -= 1
            print("No has adivinado la letra :(")


        #Comprobamos si has adivinado la palabra
        if "_" not in seguimiento_palabra:
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_elegida}")
            print(f"La palabra era {palabra_elegida}")
            break
    else:
        print(f"Has perdido. La palabra era: {palabra_elegida}")

ahorcado()