def remove_repetidos(lista: list) -> list:
    lista_cache = []
    for elemento in lista:
        if elemento not in lista_cache:
            lista_cache.append(elemento)
    return sorted(lista_cache)


if __name__ == '__main__':
    lista = [2, 4, 2, 2, 3, 3, 1]
    print(remove_repetidos(lista))

    print(remove_repetidos([1, 2, 3, 3, 3, 4]))
