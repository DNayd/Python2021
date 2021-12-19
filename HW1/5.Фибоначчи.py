x = int(input('Введите простое число'))
def primenumb(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1
def search_prime(z):
    while z >= 2:
        if primenumb(z) == 1:
            return z
        else:
          z -= 1
def Fib(f1, f2):
    print(f1, f2, '', end='')
    for i in range(1, 14):
        F = f1 + f2
        f1 = f2
        f2 = F
        print(f2, '', end='')
F1 = search_prime(x - 1)
F2 = search_prime(x)
Fib(F1, F2)
