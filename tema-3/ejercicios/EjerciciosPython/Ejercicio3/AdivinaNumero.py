import random
from xml.etree.ElementTree import tostring

print("Ok " + input(" What´s your name? ") + " I’ve thought of a number between 1 and 100, and you only have eight attempts to guess what you think the number is.")


numeroAleatorio = random.randint(1, 100)

for i in range (8):

    numeroUsuario = int( input(f"Attempt {i} . What number do you say? ") )

    if numeroUsuario < 1 or numeroUsuario > 100:
        print("Number not valid. Say a number between 1 to 100")
        i+=1
    elif numeroUsuario < numeroAleatorio:
        print("Your chosen was lees than the correct number")
        i += 1
    elif numeroUsuario > numeroAleatorio:
        print("Your chosen was upper then the correct number")
        i += 1
    elif numeroUsuario == numeroAleatorio:
        print(f"Congrats your chose the correct number, in {i} attemps")
        exit()
