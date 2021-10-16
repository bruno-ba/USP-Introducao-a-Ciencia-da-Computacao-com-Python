"""
Exercício 3

Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. Observe o exemplo abaixo:

Exemplo 1:

    Entrada de Dados:

Digite um número inteiro: 78615

    Saída de Dados:

O dígito das dezenas é 1

Exemplo 2:

    Entrada de Dados:

Digite um número inteiro: 2

    Saída de Dados:

O dígito das dezenas é 0

Dica: O operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor. O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.
"""


def get_digito_dezenas(num: int) -> int:
    '''
    :param num:
    :return:

    >>> get_digito_dezenas(123)
    2
    >>> get_digito_dezenas(1246543)
    4
    >>> get_digito_dezenas(124654378897897)
    9
    '''

    dv, md = divmod(num, 10)
    dv, md = divmod(dv, 10)
    return md


if __name__ == '__main__':
    num = int(input('Digite um número inteiro: '))
    print(f'O dígito das dezenas é {get_digito_dezenas(num)}')

