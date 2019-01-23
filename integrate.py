# Вычисление численного значения инеграла
# Методом Ньюта-Котеса

# импортируем библиотеки
import numpy as np 
import matplotlib.pyplot as mpl

# Исследуемая функция
def f(x):
    return -0.1*x**3+0.14*x**2+1.5*x-1.64

def f_xk(a, b, t):
    return (a + b)/2 + (b - a)*t/2

# Интервал поиска интеграла функции
a = -4
b = 4
# Количество точек для нахождения интеграла
n = 4
# Первые четыре коэффициента Нюта-Котеса
# КОторые дают точно находить интеграл для полинома n-1 порядка (т.е) 4-1 = 3
c = [1/4, 3/4, 3/4, 1/4]

# Находим опорные точки на отрезке -1, 1 
# которые расположены на расстоянии 2/(n-1) друг от друга
t = []
for i in np.arange(-1, 1.01, 2/(n-1)):
    t.append(i)

# Переходим от координат -1, 1 к нашим координатам a, б
x = []
for i in t:
    x.append(f_xk(a, b, i))

# Ищем наш интеграл по формуле 3.20
res = 0
for i in range(0, 4):
    res = res + c[i] * f(x[i])   
res = res * (b - a)/2

print("integral = {0}".format(res))

# Рисуем граффик (хз зачем)
t = np.arange(-1, 1+0.01, 2/(4-1))
x = []
for i in t:
    x.append(f_xk(a, b, i))
y = [f(y) for y in x]

mpl.plot(np.arange(a, b+0.01, 0.1),f(np.arange(a, b+0.01, 0.1)))
mpl.plot(x, y, 'go')
mpl.show()