def fizz_buzz_3(num):
    if num % 3 ==0 and num % 5 == 0:
        return 'FizzBuzz'
    return num


if __name__ == '__main__':
    num = int(input('Digite um número: '))
    print(fizz_buzz_3(num))
