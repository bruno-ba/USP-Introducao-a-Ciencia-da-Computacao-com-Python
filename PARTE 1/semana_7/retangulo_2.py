

def gerar_retangul_2(largura:int, altura:int)->str:
    for x in range(altura):
        for y in range(largura):
            char_print = "#" if x == 0 or x == altura - 1 or y == 0 or y == largura - 1 else ' '
            print(char_print, end='')
        print()


def main():
    while True:
        try:
            largura = int(input('digite a largura: '))
            altura = int(input('digite a altura: '))
        except ValueError:
            continue
        else:
            gerar_retangul_2(largura, altura)
            break


if __name__ == '__main__':
    main()
