"""
Exercício 2

Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

Exemplo:

    Entrada de Dados:

Digite a primeira nota: 4

Digite a segunda nota: 5

Digite a terceira nota: 6

Digite a quarta nota: 7

    Saída de Dados:

A média aritmética é 5.5
"""


def media_aritimetica(*args):
    '''

    :param args:
    :return:

    >>> media_aritimetica(10, 10 , 10, 10)
    10.0
    '''
    return sum(args) / len(args)


if __name__ == '__main__':
    notas = {'primeira': 0, 'segunda': 0, 'terceira': 0, 'quarta': 0}

    for k, v in notas.items():
        notas[k] = float(input(f'Digite a {k} nota: '))

    media = media_aritimetica(*notas.values())

    print(f'A média aritmética é {media}')
