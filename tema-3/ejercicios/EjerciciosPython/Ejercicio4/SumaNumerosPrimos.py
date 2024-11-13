

def es_Primo(numero):

    primo = False
    suma = 0

    if numero < 2:
        primo = False

    for i in range (2, numero):
        if (numero % i) == 0:
            primo = False
        else:
            primo = True



    return primo


def suma_primos(numero):

    suma = 0

    for i in range (numero):
        if ( es_Primo(i) == True):
            suma +=  i

    print(suma)


suma_primos(11)
