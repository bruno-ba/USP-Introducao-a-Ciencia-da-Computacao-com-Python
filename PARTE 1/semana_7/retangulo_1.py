

def gerar_retangul_1(largura:int, altura:int)->str:
    for _ in range(altura):
        for _ in range(largura):
            print('#', end='')
        print()


def main():
    while True:
        try:
            largura = int(input('digite a largura: '))
            altura = int(input('digite a altura: '))
        except ValueError:
            continue
        else:
            gerar_retangul_1(largura, altura)
            break


if __name__ == '__main__':
    main()
