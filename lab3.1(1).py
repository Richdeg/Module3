#для параметризации функции
from sympy import *

#для построения на графиков
import matplotlib.pyplot as plt
import numpy


#метод Ньютона
def nyton(y, a, b, h):
    s = 0
    while round(a, 8) < b:
        s += (h / 8) * (y.evalf(subs={'x': a}) + 3 * y.evalf(subs={'x': a + h / 3}) + 3 * y.evalf(subs={'x': a + h / 1.5}) + y.evalf(subs={'x': a + h}))
        a += h
    return s

#функция p(x) на отрезке
x = symbols('x')
p = 1 + x * 0
a, b = 0, 1

#функция q(y) на отрезке
q = 1 + x * 0
c, d = 1, 3

h = 0.01 #шаг

P = 1 / nyton(p, a, b, h)
Q = 1 / nyton(q, c, d, h)
print(P)
print(Q)

#множество элементарных исходов случайной величины Z=X+Y
print(P * p * Q * q)

#плотность вероятности суммы случайных величин Z=X+Y
def f(z):
    if b + c <= z <= b + d:
        return nyton(P * p * Q * q.evalf(subs={'x': z - x}), a, b, h)
    else:
        return 0

print(f(2))

#графики плотностей вероятности
def p_func(x):
    if a < x < b: return p.evalf(subs={'x': x})
    else: return 0
def q_func(y):
    if c < y < d: return p.evalf(subs={'x': y})
    else: return 0

xi = numpy.linspace(-1, 7, 100)
X = [p_func(i) for i in xi]
plt.plot(xi, X)
plt.xlabel('x')
plt.ylabel('p(x)')
plt.show()

yi = numpy.linspace(-1, 7, 100)
Y = [q_func(i) for i in yi]
plt.plot(yi, Y)
plt.xlabel('y')
plt.ylabel('q(y)')
plt.show()

zi = numpy.linspace(-1, 7, 100)
Z = [f(i) for i in zi]
plt.plot(zi, Z)
plt.xlabel('z')
plt.ylabel('f(z)')
plt.show()

#полная вероятность для случайной величины Z
h = 0.5
min = a + c
max = b + d
sum = 0
while round(min, 8) < max:
    sum += (h / 8) * (f(min) + 3 * f(min + h / 3) + 3 * f(min + h / 1.5) + f(min + h))
    min += h
print(sum)
