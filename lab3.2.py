import math
from sympy import *
import numpy
import matplotlib.pyplot as plt
from Project1 import Gaussa

#задаем функции для дифференциального уравнения вида y" + py' + qy = f
def p(x): return -5 + x * 0
def q(x): return 6 + x * 0
def f(x): return math.exp((3 * x)) + x
x = [0, 3]
y = [2, 4]
n = 30 #число интервалов

def reshenie(p, q, f, x, y, n):
    h = (x[1] - x[0]) / n #шаг
    N = n - 1
    A = numpy.zeros([N, N])
    A[0, 0] = h ** 2 * q(x[0] + h) - 2
    A[0, 1] = 1 + 0.5 * h * p(x[0] + h)
    A[N - 1, N - 2] = 1 - 0.5 * h * p(x[1] - h)
    A[N - 1, N - 1] = h ** 2 * q(x[1] - h) - 2
    xi = x[0] + h
    for i in range(1, N - 1):
        xi += h
        A[i, i - 1] = 1 - 0.5 * h * p(xi)
        A[i, i] = h ** 2 * q(xi) - 2
        A[i, i + 1] = 1 + 0.5 * h * p(xi)
    B = numpy.zeros([N])
    B[0] = h ** 2 * f(x[0] + h) - y[0] * (1 - 0.5 * h * p(x[0] + h))
    B[N - 1] = h ** 2 * f(x[1] - h) - y[1] * (1 + 0.5 * h * p(x[1] - h))
    xi = x[0] + h
    global mas_xi
    mas_xi = [xi]
    for i in range(1, N - 1):
        xi += h
        mas_xi.append(xi)
        B[i] = h ** 2 * f(xi)
    mas_xi.append(x[1] - h)
    #с помощью метода Гаусса находим yi
    global yi
    yi = []
    for j in Gaussa.Metod_Gaussa(A, B):
        yi.append(float(j))
    point = [[] for i in range(len(yi))]
    for i in range(len(yi)):
        point[i].append(mas_xi[i])
        point[i].append(yi[i])
    return point

print(reshenie(p, q, f, x, y, n))

#копирование списков на будущее
xii = mas_xi[:]
yii = yi[:]

#график
mas_xi.insert(0, x[0]), yi.insert(0, y[0])
mas_xi.append(x[1]), yi.append(y[1])
plt.plot(mas_xi, yi)
plt.grid()
plt.show()

#приблизительная оценка погрешности посредством построения интерполяционного полинома Ньютона
def interp(xi, yi):
    #создаем список для записи значений функции и конечных разностей
    dy = [[] for i in range(len(xi))]
    #записываем в список значения функции в каждой из опорных точек
    for i in yi: dy[0].append(i)
    #заполнение списка значениями конечных разностей
    for j in range(0, len(dy) - 1):
        for i in range(len(dy[j]) - 1):
            dy[j + 1].append(dy[j][i + 1] - dy[j][i])

    #вычисляем многочлен
    def multi(n):
        mul = 1
        for j in range(n):
            mul *= (xx - xi[j])
        return mul
    f = dy[0][0]
    for i in range(1, len(xi)):
        f += dy[i][0] * multi(i)/ (math.factorial(i) * (xi[1] - xi[0]) ** i)
    return f

xx = symbols('xx')
e = min(abs(interp(xii, yii).evalf(subs={'xx': x[0]}) - y[0]), abs(interp(xii, yii).evalf(subs={'xx': x[1]}) - y[1]))
print(e)
