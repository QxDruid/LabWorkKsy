# Аппроксимация методом наименьших квадратов (линейная a*x+b)
from matplotlib import pyplot as mpl
import numpy as np

# Апроксимируемая функция
def f(x):
    return 5/9*x

# Функция нахождения Y по кординтам X и найденным коэффициентам a и b
def line_f(a, b, x):
    return a*x+b

# Начальные условия

# Количество точек для апроксимации
app_points = 10
# Интервал нахождения функции
min = -5
max = 5
# Шаг точек интерполяции
step = (max - min)/(app_points)

# Записываем опорные точки интерпляции по нашей реальной функции
points_x = np.arange(min, max+0.01, step)
print(points_x)
points_y = [f(x) for x in points_x]
print(points_y)

# Все необходимое для поиска A и B 
x = 0
for i in points_x:
    x = x + i
x = 1/len(points_x) * x
print(x)

y = 0
for i in points_x:
    y = y + f(i)
y = 1/len(points_x) * y
print(y)

x2 = 0
for i in points_x:
    x2 = x2 + i**2
x2 = 1/len(points_x) * x2
print(x2)


yx = 0
for i in points_x:
    yx = yx + i * f(i)
yx = 1/len(points_x) * yx
print(yx)


# Рассчет коэффициентов по найденным ранее значениям
b = (x2 * y - yx * x)/(x2 - x**2)
a = (yx + x*y) / (x2 - x**2)

# Вывод коэффициентов
print(a, b)

# Точки построения граффика
plot_x = np.arange(min,max,0.01)
# Истинная функция
func_y = [f(x) for x in plot_x]
# Интерполяция функции
interpolate_y = [line_f(a,b,x) for x in plot_x]

# Вывод граффика на экран
mpl.plot(plot_x, func_y) # печать граффика функции
mpl.plot(plot_x, interpolate_y) # печать интерполяционного граффика
mpl.plot(points_x, points_y, 'go') # печпть узлов интерполяции
mpl.legend(['function', 'interpolation', 'base points']) # вывод легенды
mpl.show()