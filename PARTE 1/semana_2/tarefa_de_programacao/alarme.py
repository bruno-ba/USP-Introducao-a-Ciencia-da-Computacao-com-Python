

if __name__ == '__main__':
    while True:
        temp = int(input('Qual temperatura? '))
        if temp >= 50:
            print('Acionar alarme!!!!')
        else:
            print('Tranquilo')