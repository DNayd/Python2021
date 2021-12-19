from math import pi, tan, sqrt
print('Калькулятор для вычисления площадей круга (1), многоугольника (2), треугольника (3),'
      'прямоугольника (4) и  трапеции (5)')
figure = input('Выберите фигуру: ')

if figure == '1':
    r = float(input('Радиус круга R = '))
    print('Площадь круга= %.2f' % (pi * r ** 2))
elif figure == '2':
    print('Длина и количество граней многоугольника:')
    a = float(input('a = '))
    n = float(input('количество граней = '))
    s = n * (l ** 2) / (4 * tan(pi / n))
    print('Площадь правильного многоугольника = %.2f' % s)
elif figure == '3':
    print('Длины сторон треугольника:')
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print('Площадь треугольника = %.2f' % s)
elif figure == '4':
    print('Длины сторон прямоугольника:')
    a = float(input('a = '))
    b = float(input('b = '))
    print('Площадь прямоугольника = %.2f' % (a * b))
elif figure == '5':
    print('Длины сторон трапеции и ее высота:')
    a = float(input('a = '))
    b = float(input('b = '))
    h = float(input('h = '))
    print('Площадь трапцеии = %.2f' % (((a + b) / 2) * h))
else:
    print('Ошибка ввода')
