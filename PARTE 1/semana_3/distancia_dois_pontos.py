if __name__ == '__main__':
    numero_1 = int(input('digite um número: '))
    numero_2 = int(input('digite um número: '))
    numero_3 = int(input('digite um número: '))
    numero_4 = int(input('digite um número: '))

    msg = 'longe' if (((numero_1 - numero_3) ** 2) + ((numero_2 - numero_4) ** 2)) ** 0.5 >= 10 else 'perto'
    print(msg)
