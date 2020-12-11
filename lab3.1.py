#библиотека для параметризации функции
from sympy import *

#метод левых прямоугольников
def left_rectangle(y, ab, N):
    a, b = ab[0], ab[1]
    h = (b - a) / N #шаг
    s = 0
    while round(a, 8) < b:
        s += h * y.evalf(subs={'x': a})
        a += h
    return s

#метод правых прямоугольников
def right_rectangle(y, ab, N):
    a, b = ab[0], ab[1]
    h = (b - a) / N #шаг
    s = 0
    while round(a + h, 8) < b:
        s += h * y.evalf(subs={'x': a + h})
        a += h
    return s

#метод средних прямоугольников
def middle_rectangle(y, ab, N):
    a, b = ab[0], ab[1]
    h = (b - a) / N #шаг
    s = 0
    while round(a, 8) < b:
        s += h * y.evalf(subs={'x': a + h / 2})
        a += h
    return s

#метод трапеций
def trapeze(y, ab, N):
    a, b = ab[0], ab[1]
    h = (b - a) / N #шаг
    s = 0
    while round(a, 8) < b:
        s += 0.5 * h * (y.evalf(subs={'x': a}) + y.evalf(subs={'x': a + h}))
        a += h
    return s

#метод Симпсона
def simpson(y, ab, N):
    a, b = ab[0], ab[1]
    h = (b - a) / N #шаг
    s = 0
    while round(a, 8) < b:
        s += (h / 6) * (y.evalf(subs={'x': a}) + 4 * y.evalf(subs={'x': a + h / 2}) + y.evalf(subs={'x': a + h}))
        a += h
    return s

#метод Ньютона
def nyton(y, ab, N):
    a, b = ab[0], ab[1]
    h = (b - a) / N #шаг
    s = 0
    while round(a, 8) < b:
        s += (h / 8) * (y.evalf(subs={'x': a}) + 3 * y.evalf(subs={'x': a + h / 3}) + 3 * y.evalf(subs={'x': a + h / 1.5}) + y.evalf(subs={'x': a + h}))
        a += h
    return s

#вывод
x = symbols('x')
y = 2 * x ** 3
ab = [0, 4]
N = 10

print(left_rectangle(y, ab, N))
print(right_rectangle(y, ab, N))
print(middle_rectangle(y, ab, N))
print(simpson(y, ab, N))
print(nyton(y, ab, N))
