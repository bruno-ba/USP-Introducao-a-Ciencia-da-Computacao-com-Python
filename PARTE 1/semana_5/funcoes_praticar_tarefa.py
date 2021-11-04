def fizzbuzz(numero):
    """
    Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

    'Fizz' se o número for divisível por 3 e não for divisível por 5;
    'Buzz' se o número for divisível por 5 e não for divisível por 3;
    'FizzBuzz' se o número for divisível por 3 e por 5;

    :param numero:
    :return:

    >>> fizzbuzz(3)
    'Buzz'
    >>> fizzbuzz(5)
    'Fizz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    >>> fizzbuzz(4)
    4
    """
    def divisivel_por_5(num):
        return num % 5 == 0

    def divisivel_por_3(num):
        return num % 3 == 0

    if divisivel_por_3(numero) and divisivel_por_5(numero):
        return 'FizzBuzz'

    elif divisivel_por_5(numero) and not divisivel_por_3(numero):
        return 'Buzz'

    elif divisivel_por_3(numero) and not divisivel_por_5(numero):
        return 'Fizz'
    else:
        return numero


def maximo(numero_1, numero_2, numero_3):
    """
    Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos,
    para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.
    :param numero:
    :return:
    >>> maximo(1, 2, 3)
    3
    >>> maximo(5, 10, 6)
    10
    """
    return max([numero_1, numero_2, numero_3])
