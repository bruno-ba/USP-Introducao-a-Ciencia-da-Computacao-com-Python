"""
Exercício 1

Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

Exemplos:
Digite um número inteiro: 13
primo

Digite um número inteiro: 12
não primo
"""


if __name__ == '__main__':
    num = int(input('Digite um número inteiro: '))
    is_primo = True

    for x in range(2, num):
        if num % x == 0:
            is_primo = False
            break

    print(f'{"primo" if is_primo else "não primo"}')