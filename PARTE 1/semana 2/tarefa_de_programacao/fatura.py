"""
Uma empresa de cartão de crédito envia suas faturas por email com a seguinte mensagem:
Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima. Note que o programa imprime a saída em duas linhas diferentes. Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Digite o nome do cliente: Fulano de Tal
Digite o dia de vencimento: 9
Digite o mês de vencimento: Janeiro
Digite o valor da fatura: 350,00

Saída de Dados:
Olá, Fulano de Tal
A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
"""


if __name__ == '__main__':
    dados = {'nome do cliente': None, 'dia de vencimento': None, 'mês de vencimento': None, 'valor da fatura': None}
    for k in dados:
        dados[k] = input(f'Digite o {k} do cliente: ')

    msg = f"""Olá, {dados.get('nome do cliente', 'inválido!')}
A sua fatura com vencimento em {dados.get('dia de vencimento', 'inválido!')} de {dados.get('mês de vencimento', 'inválido!')} no valor de R$ {dados.get('valor da fatura', 'inválido!')} está fechada."""

print(msg)