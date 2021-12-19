x = int(input('Введите целое число'))
def primenumb(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1
while x >= 2:
    if primenumb(x) == 1:
        print('Максимальное простое, которое меньше заданного =', x)
        break
    else:
        x -= 1
