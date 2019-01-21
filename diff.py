# Диффернцирование методом Логранжа
# Для построения графика производной, разбиваем наш интервал на отрезки
# и находим значения дифференциала на кажом из них

 # импортируем библиотеки
import numpy as np 
import math
import matplotlib.pyplot as mpl

def f(x):
    return 5*x**3+6**2-3



# Количество опорных точек для нахождения производных
diff_points = 10

# Интервал нахождения функции
min = -5
max = 5

# На сколько отрезков будет делиться наш интервал
split_points = 100
# Размер дифференцируемых отрезков
split_step = (max - min)/(split_points-1)

# Порядок производной (Дожжен быть меньше чем количество )
m = 2



diff_res = []
x = []

# Устанавливаем начало первого отрезка
a = min
b = a
while b <= max:
    # Устанавливаем конец отрезка
    b = a + split_step
    # Находим середину отрезка (координату x) для построения графика f'(x)
    x.append(a + (b-a)/2)
    # Находим все опорные точки дифференцирования внутри интервала a, b
    points_x = np.arange(a, b, (b - a) / (diff_points-1))
    diff = 0

    # Циклы это формула из учебника (Для метода Логранжа 
    # при порядке дифференцирования меньшем числу опорных точек)
    for i in range(0, m+1, 1):
        x_summ = 1
        for j in range(0, m+1, 1):
            if i == j:
                continue
            else:
                x_summ = x_summ * (1/(points_x[i]-points_x[j]))
        diff = diff + f(points_x[i]) * x_summ
    diff_res.append(math.factorial(m)*diff)
    a = b
# Выводим граффик реальной функции и граффик производной
real_x = np.arange(min, max, 0.1)
real_y = [f(x) for x in real_x]

mpl.plot(real_x, real_y)
mpl.plot(x,diff_res)
mpl.show()

