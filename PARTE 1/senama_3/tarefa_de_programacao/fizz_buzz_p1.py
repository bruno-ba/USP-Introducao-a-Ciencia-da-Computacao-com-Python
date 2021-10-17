def fizz_buzz_1(num):
    if num % 3 == 0:
        return 'Fizz'
    return num


if __name__ == '__main__':
    num = int(input('Digite um número: '))
    print(fizz_buzz_1(num))
