def fizz_buzz_1(num):
    if num % 3 == 0:
        return 'Fizz'
    return num


def fizz_buzz_2(num):
    if num % 5 == 0:
        return 'Buzz'
    return num


def fizz_buzz_3(num):
    if num % 3 ==0 and num % 5 == 0:
        return 'FizzBuzz'
    return num