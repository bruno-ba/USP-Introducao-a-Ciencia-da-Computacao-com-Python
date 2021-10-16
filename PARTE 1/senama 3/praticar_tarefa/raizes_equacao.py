
if __name__ == '__main__':
    a = int(input('Digite a: '))
    b = int(input('Digite b: '))
    c = int(input('Digite c: '))
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print('esta equação não possui raízes reais')
    else:
        raiz_x = (-b + (delta ** 0.5)) / (2 * a)
        if delta == 0:
            print(f'a raiz dupla desta equação é {raiz_x}')
        else:
            raiz_y = (-b - (delta ** 0.5)) / (2 * a)
            if raiz_x >= raiz_y:
                print(f'as raízes da equação são {raiz_x} e {raiz_y}')
            else:
                print(f'as raízes da equação são {raiz_y} e {raiz_x}')