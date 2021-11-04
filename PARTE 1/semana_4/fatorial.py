"""
Exercício 1

Escreva um programa que receba um número natural n n n na entrada e imprima n! n! n! (fatorial) na saída.
Exemplo:
Digite o valor de n: 5
120
"""

if __name__ == '__main__':

    fatorial = 1

    num = int(input(f'Digite o valor de n: '))

    for i in range(1, num + 1):
        fatorial *= i

    print(fatorial)