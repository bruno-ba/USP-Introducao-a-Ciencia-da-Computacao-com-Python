if __name__ == '__main__':
    numero_1 = int(input('digite um número: '))
    numero_2 = int(input('digite um número: '))
    numero_3 = int(input('digite um número: '))

    msg = 'crescente' if numero_1 < numero_2 < numero_3 else 'não está em ordem crescente'
    print(msg)
