"""
Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

    Entrada de Dados:

Por favor, entre com o número de segundos que deseja converter: 178615

    Saída de Dados:

2 dias, 1 horas, 36 minutos e 55 segundos.
"""


if __name__ == '__main__':
    partes_tempo = { }
    total_seg = int(input('Por favor, entre com o número de segundos que deseja converter: '))
    total_minutos, segundos = divmod(total_seg, 60)
    partes_tempo.setdefault('segundos', segundos)
    total_horas, minutos = divmod(total_minutos, 60)
    partes_tempo.setdefault('minutos', minutos)
    total_dias, horas = divmod(total_horas, 24)
    partes_tempo.setdefault('horas', horas)
    partes_tempo.setdefault('dias', total_dias)

    msg =f'{partes_tempo.get("dias")} dias, {partes_tempo.get("horas")} horas, {partes_tempo.get("minutos")} minutos e {partes_tempo.get("segundos")} segundos.'
    print(msg)
