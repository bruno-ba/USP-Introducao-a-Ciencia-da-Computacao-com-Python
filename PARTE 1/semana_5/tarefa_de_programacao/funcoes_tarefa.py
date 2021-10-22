def maior_primo(num):
    def is_primo(n):
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

    primos = [x for x in range(2, num+1) if is_primo(x)]

    return max(primos)


def maximo(n1, n2):
    return max(n1, n2)


def vogal(letra: str):
    return (str(letra)).lower() in ['a', 'e', 'i', 'o', 'u']


if __name__ == '__main__':
   print(maior_primo(100))

   print(maximo(100, 789))

   print(vogal('a'))