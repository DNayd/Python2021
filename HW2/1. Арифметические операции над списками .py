import numpy as np
from operator import add, sub, mul, truediv

def calc (l, u):
  a = l[0]
  b = l[1]
  calcul = u(a,b)
  for i in range(2, len(l)):
    a = calcul
    b = l[i]
    calcul = u(a,b)
  return calcul

def power(l,Pwr):
  return [x ** Pwr for x in l]

def sqrt(l,Sq):
  return [x ** 1/Sq for x in l]

def log(l):
  g = np.log(l)
  return g

x = int(input('Сколько списков необходимо пересчитать? '))
lists = []

for i in range(x):
    z = [i]
    z = list(map(int, input('Введите значения списков: ').split()))
    lists.append(z)

for i in range(len(lists)):
    while len(lists[i]) < len(max(lists, key=len)):
        lists[i].append(0)
print(lists)
lists = np.array(lists)

print(calc(lists, add))
print(calc(lists, sub))
print(calc(lists, mul))
print(calc(lists, truediv))
print(power(lists, int(input('Степень: '))))
print(sqrt(lists, int(input('Степень корня: '))))
print(log(lists))

