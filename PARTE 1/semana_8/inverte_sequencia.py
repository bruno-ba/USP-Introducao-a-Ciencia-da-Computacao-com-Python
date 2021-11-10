
if __name__ == '__main__':
    numeros_digitados = []
    while True:
        num = int(input('Digite um número: '))
        if num == 0:
            break
        numeros_digitados.append(num)

    for numero in numeros_digitados[::-1]:
        print(numero)

