
def alternar_jogada(*args):
    cache_jogada = list(args)
    cont = 0
    while True:
        yield cache_jogada[cont % len(cache_jogada)]
        cont += 1


def computador_escolhe_jogada(n, m):
    max_pecas_para_retirar = min(m, n)
    for num_pecas in reversed(range(1, max_pecas_para_retirar + 1)):
        if (n - num_pecas) % (m + 1) == 0:
            return num_pecas
    return max_pecas_para_retirar


def usuario_escolhe_jogada(n, m):
    while True:
        try:
            num_pecas = int(input('Quantas peças você vai tirar? '))
        except ValueError:
            continue
        else:
            if num_pecas == 0 or num_pecas > m:
                print('Oops! Jogada inválida! Tente de novo.')
                continue
            return num_pecas


def validar_partida():
    while True:
        try:
            n = int(input("Quantas peças? "))
            m = int(input("Limite de peças por jogada? "))
        except ValueError:
            continue
        else:
            if 1 <= m <= n:
                return n, m
            print('Valores inválidos para iniciar a partida!')


def definir_jogada_inicial(n, m):
    if n % (m + 1) == 0:
        print("Você começa!")
        return usuario_escolhe_jogada, computador_escolhe_jogada
    print("Computador começa!")
    return computador_escolhe_jogada, usuario_escolhe_jogada


def partida():
    n, m = validar_partida()
    jogada_inicial, jogada_seguinte = definir_jogada_inicial(n, m)
    for func in alternar_jogada(jogada_inicial, jogada_seguinte):
        is_pc = func is computador_escolhe_jogada
        while True:
            pecas_retiradas = func(n, m)
            n -= pecas_retiradas
            msg_jogada = 'O computador ' if is_pc else 'Você '
            msg_pecas = f'tirou uma peça.' if pecas_retiradas == 1 else f'tirou {pecas_retiradas} peças.'
            print(msg_jogada + msg_pecas)
            if n > 0:
                msg_tabuleiro = f'Agora resta apenas uma peça no tabuleiro.\n' if n == 1 else f'Agora restam {n} peças no tabuleiro.\n'
                print(msg_tabuleiro)
            break

        if n == 0:
            msg_ganhador ='Fim do jogo! O computador ganhou!\n' if is_pc else 'Fim do jogo! Você ganhou!\n'
            print(msg_ganhador)
            break


def campeonato():
    for x in range(1, 4):
        print(f'**** Rodada {x} ****\n')
        partida()
    print('''**** Final do campeonato! ****

Placar: Você 0 X 3 Computador''')


if __name__ == '__main__':

    print("Bem-vindo ao jogo do NIM! Escolha:")
    while True:
        escolha = input('''1 - para jogar uma partida isolada
2 - para jogar um campeonato ''')
        if escolha not in ['1', '2']:
            continue
        break
    if escolha == '1':
        print('Voce escolheu uma partida isolada!\n')
        partida()
    else:
        print('Voce escolheu um campeonato!\n')
        campeonato()



