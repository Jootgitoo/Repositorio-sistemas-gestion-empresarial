import random

def sumOfPrime(a):
    result = 0
    for i in range(0, a+1):
        if isPrime(i):
            result += i

    return result

def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True

#HANGED

def hanged(palabra, guessed_letters):
    cadena = ""
    for letter in palabra:
        if letter in guessed_letters:
            cadena += letter  # Si la letra ha sido adivinada, se muestra
        else:
            cadena += "-"  # Si no, se muestra un guión
    return cadena

# Colección de palabras para el juego
coleccionOfWords = ["PALABRA", "CASA", "PELOTA", "ORDENADOR"]
num = random.randint(0, len(coleccionOfWords) - 1)
word = coleccionOfWords[num]
lives = 6
guessed_letters = []

print("Palabra a adivinar:", hanged(word, guessed_letters))

while lives > 0:
    letter = input("Introduce una letra para comprobar si existe en la palabra: ").upper()

    guessed_letters.append(letter)

    # Mostramos el estado actual de la palabra
    current_state = hanged(word, guessed_letters)
    print("Palabra: ", current_state)

    # Comprobamos si la letra está en la palabra
    if letter not in word:
        lives -= 1
        print(f"La letra '{letter}' no está en la palabra. Te quedan {lives} vidas.")

    # Comprobamos si el usuario ha adivinado toda la palabra
    if current_state == word:
        print("¡Ganaste! La palabra es " + word)
        break

    # Permitimos al usuario intentar adivinar la palabra completa
    wordPlayer = input("¿Cuál es la palabra?: ").upper()
    if word == wordPlayer:
        print("¡Ganaste! La palabra es " + wordPlayer)
        break
    else:
        print("¡Esa no es la palabra! Inténtalo de nuevo.")
        lives -= 1

if lives == 0:
    print("Lo siento, te quedaste sin vidas. La palabra era: " + word)

