def fizz_buzz_2(num):
    if num % 5 == 0:
        return 'Buzz'
    return num


if __name__ == '__main__':
    num = int(input('Digite um número: '))
    print(fizz_buzz_2(num))
