# Variable para guardar el texto
from ast import Param

text = input("Tell me a text: ")

EXIST_PYTON = "python"

#-----------------------------------------------------------------------------------------------------------------------
#APARTADO 1
print("APARTADO 1")

#Variables para guardar las letras que queramos
letter1 = str( input("Tell me a letter: ") )
letter2 = str( input("Tell me a letter: ") )
letter3 = str( input("Tell me a letter: ") )

#Contador de las letras (uno para cada letra)
contLetter1 = 0
contLetter2 = 0
contLetter3 = 0

#Recorre el text caracter a caracter y si la letra del texto coincide con letter1 o letter2 o letter3 añade 1 al contador
text = text.upper()
for i in range (0, len(text) ):
    if text[i] == letter1.upper():
        contLetter1+=1
    elif text[i] == letter2.upper():
        contLetter2+=1
    elif text[i] == letter3.upper():
        contLetter3+=1

#Imprimimos cuantas veces aparece cada letra
print("The letter " + letter1 + " appear " + str(contLetter1) + " times")
print("The letter " + letter2 + " appear " + str(contLetter2) + " times")
print("The letter " + letter3 + " appear " + str(contLetter3) + " times")

print("")

#-----------------------------------------------------------------------------------------------------------------------
#APARTADO 2
print("APARTADO 2")

#Divido el contenido de text por palabras
palabras = text.split()

#numeroPalabras = a las palabras que tenga palabras
numeroPalabras = len(palabras)

print("The text have " + str(numeroPalabras) + " words")

print("")

#-----------------------------------------------------------------------------------------------------------------------
#APARTADO 3
print("APARTADO 3")

primeraLetra = text[0]
ultimaLetra = text[-1]

print("The first letter was: " + str(primeraLetra) )
print("The second letter was: " + str(ultimaLetra) )

print("")
#-----------------------------------------------------------------------------------------------------------------------
#APARTADO 4
print("APARTADO 4")

print( text[::-1] )

print("")
#-----------------------------------------------------------------------------------------------------------------------
#APARTADO 5
print("APARTADO 5")

if EXIST_PYTON in text.lower():
    print("The word python exist")
else:
    print("The word python doesn´t exist")

print()
#-----------------------------------------------------------------------------------------------------------------------
