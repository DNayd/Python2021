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

print('Калькулятор для сложения (1), вычитания (2), умножения (3),'
      'деления (4), возведения в степень (5), извлечения корня (6) и логарифмирования (7)')
action = input('Выберите действие: ')

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

if action == '1':
  print(calc(lists, add))
elif action == '2':
  print(calc(lists, sub))
elif action == '3':
  print(calc(lists, mul))
elif action == '4':
  print(calc(lists, truediv))
elif action == '5':
  print(power(lists, int(input('Степень: '))))
elif action == '6':
  print(sqrt(lists, int(input('Степень корня: '))))
elif action == '7':
  print(log(lists))
else:
  print('Ошибка ввода')

