

def es_Primo(numero):

    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if (numero % i) == 0:
            return False
    return True

def suma_primos(numero):
    suma = 0

    for numero in range(2, numero + 1):
        if es_Primo(numero):
            suma += numero


    print(suma)


suma_primos(11)
