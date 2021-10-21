"""
Exercício 2 - Desafio do vídeo "Repetição com while"

Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

Exemplos:

Digite um número inteiro: 12345
não

Digite um número inteiro: 1011
sim
"""

if __name__ == '__main__':
    has_num_adjacentes = False
    num = int(input('Digite um número inteiro: '))

    while True:
        if num < 10:
            break

        _, dois_ultimos_digitos = divmod(num, 100)
        penultimo_digito, ultimo_digito = divmod(dois_ultimos_digitos, 10)

        if penultimo_digito == ultimo_digito:
            has_num_adjacentes = True
            break

        num, _ = divmod(num, 10)

    print(f'{"sim" if has_num_adjacentes else "não"}')