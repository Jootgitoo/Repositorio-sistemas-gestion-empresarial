

def es_Primo(numero):

    primo = False

    if numero < 2:
        primo = False

    for i in range (2, numero):
        if (numero % i) == 0:
            primo = False
        else:
            primo = True

    return primo


print( es_Primo(11) )

TERMINAR EJERCICIO 4