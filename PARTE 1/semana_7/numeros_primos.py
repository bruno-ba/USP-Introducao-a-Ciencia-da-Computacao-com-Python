
def verificar_primo(numero):
    if numero == 2:
        return True

    if numero < 2 or numero % 2 == 0:
        return False

    for x in range(2, numero):
        if numero % x == 0:
            return False

    return True


def n_primos(numero: int) -> int:
    return len([x for x in range(2, numero + 1) if verificar_primo(x)])
