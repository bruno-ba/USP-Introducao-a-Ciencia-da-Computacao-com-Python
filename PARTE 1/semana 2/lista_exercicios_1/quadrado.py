"""Exercício 1
Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.

Observação: a saída deve estar no formato: "perímetro: x - área: y"

Abaixo um exemplo de como devem ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:

Digite o valor correspondente ao lado de um quadrado: 3

Saída de Dados:

perímetro: 12 - área: 9

Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez
"""


def area_perimetro(lado):
    '''
    :param lado:
    :return:

    >>> area_perimetro(5)
    (20, 25)
    >>> area_perimetro(6)
    (24, 36)
    '''

    return 4 * lado, lado ** 2


if __name__ == '__main__':
    lado = int(input('Digite o valor correspondente ao lado de um quadrado:'))
    perimetro, area = area_perimetro(lado)
    print(f'perímetro: {perimetro} - área: {area}')
