def maior_elemento(lista: list) -> int:
    maior = lista[0]
    for x in lista:
        maior = max(maior, x)
    return maior


if __name__ == '__main__':
    print(maior_elemento([x for x in range(101)]))