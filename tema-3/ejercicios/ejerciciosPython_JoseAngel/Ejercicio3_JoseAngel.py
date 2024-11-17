import random

name = input("Whats your name? ")
numberToGuess= random.randint(1,100)
print(numberToGuess)
print(name+", I am thinking of a number between 1 and 100 and you have to guess it. You have 8 tries")
cont = 8
while cont > 0:
    num = int(input("Enter a number: "))
    if num == numberToGuess:
        print(name+", you guessed it right!")
        cont = 0
    else:
        print("Noup, try again")
        cont = cont - 1
