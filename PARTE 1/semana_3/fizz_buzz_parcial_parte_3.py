if __name__ == '__main__':
    numero = int(input('digite um número: '))
    msg = 'FizzBuzz' if numero % 3 == 0 and numero % 5 == 0 else numero
    print(msg)

