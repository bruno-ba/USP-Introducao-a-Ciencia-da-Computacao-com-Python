

def par_impar(num):
    if num % 2 == 0:
        return 'par'
    return 'ímpar'


if __name__ == '__main__':
    num = int(input('Digite um número: '))
    print(par_impar(num))
