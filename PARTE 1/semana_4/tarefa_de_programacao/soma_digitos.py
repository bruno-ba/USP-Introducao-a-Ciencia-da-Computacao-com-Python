"""
Exercício 3

  Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:
"""
if __name__ == '__main__':
    num = int(input('Digite um número inteiro: '))
    soma = 0

    while True:
        num, resto = divmod(num, 10)
        soma += resto
        if num < 10:
            soma += num
            break

    print(soma)



