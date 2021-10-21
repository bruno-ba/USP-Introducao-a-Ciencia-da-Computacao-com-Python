if __name__ == '__main__':
    num = int(input('Digite o valor de n: '))
    i = 0

    while True:
        if i % 2 != 0:
            print(i)
            num -= 1

        i += 1

        if num <= 0:
            break

