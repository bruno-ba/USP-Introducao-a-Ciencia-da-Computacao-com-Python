

if __name__ == '__main__':
    x_1 = int(input('Digite o valor de x1: '))
    y_1 = int(input('Digite o valor de y1: '))
    x_2 = int(input('Digite o valor de x2: '))
    y_2 = int(input('Digite o valor de y2: '))

    delta = (((x_1 - x_2) ** 2) + ((y_1 - y_2) ** 2)) ** 0.5

    if delta >= 10:
        print('longe')
    else:
        print('perto')



