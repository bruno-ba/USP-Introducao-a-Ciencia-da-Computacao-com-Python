if __name__ == '__main__':
    p1_x = int(input('Digite a coordenada x de p1: '))
    p1_y = int(input('Digite a coordenada y de p1: '))
    p2_x = int(input('Digite a coordenada x de p2: '))
    p2_y = int(input('Digite a coordenada y de p2: '))

    distancia = (((p1_x - p2_x)**2) + ((p1_y - p2_y)**2)) ** 0.5

    if distancia >= 10:
        print('longe')
    else:
        print('perto')
