def e_hipotenusa(numero):
    for x in range(1, numero):
        for y in range(1, numero):
            if (numero ** 2) == (x ** 2) + (y ** 2):
                return True
    return False


def soma_hipotenusas(numero):
    return sum([x for x in range(1, numero + 1) if e_hipotenusa(x)])
