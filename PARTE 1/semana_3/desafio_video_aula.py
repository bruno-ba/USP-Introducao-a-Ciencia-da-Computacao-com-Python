if __name__ == '__main__':
    param_a = float(input('digite um número: '))
    param_b = float(input('digite um número: '))
    param_c = float(input('digite um número: '))

    delta = (param_b ** 2) - (4 * param_a * param_c)

    if delta < 0:
        print('esta equação não possui raízes reais')

    elif delta == 0:
        raiz_dupla = ((-param_b) + (delta ** 0.5)) / (2 * param_a)
        print(f'a raiz dupla desta equação é {raiz_dupla}')

    else:
        raiz_1 = ((-param_b) + (delta ** 0.5)) / (2 * param_a)
        raiz_2 = ((-param_b) - (delta ** 0.5)) / (2 * param_a)

        if raiz_1 < raiz_2:
            print(f'as raízes da equação são {raiz_1} e {raiz_2}')
        else:
            print(f'as raízes da equação são {raiz_2} e {raiz_1}')