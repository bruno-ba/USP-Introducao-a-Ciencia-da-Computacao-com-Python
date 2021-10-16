

if __name__ == '__main__':
    numeros = []
    n1 = int(input('Digite o primeiro número: '))
    numeros.append(n1)
    n2 = int(input('Digite o segundo número: '))
    numeros.append(n2)
    n3 = int(input('Digite o terceiro número: '))
    numeros.append(n3)

    ord_nums = sorted(numeros)

    if ord_nums == numeros:
        print('crescente')
    else:
        print('não está em ordem crescente')

