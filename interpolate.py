import numpy as np  # импортируем библиотеки    
import matplotlib.pyplot as mpl

# функция рассчета одной точки интерполяции
# с координатой X по базовымм точкам arr_x и arr_y
def lagranje_point(x, arr_x, arr_y): 
    l = [] # объявляем пустой массив
    
    # По каждой базовой точке находим базисные полиномы li(x)
    for i in range(0, len(arr_x)): 
        l.append(1)
        for j in range (0, len(arr_x)):
            # j != i потому что в этом случае деление на 0
            # значит пропускаем итерацию где i == j
            if j == i:
                continue
            l[i] = l[i] * (x-arr_x[j])/(arr_x[i] - arr_x[j])
    # находим многочлен Лагранжа по формуле
    # где Yi равняется координатам Y базовых точек
    L = 0
    for i in range(0, len(arr_x)):
        L = L + arr_y[i]*l[i]
    return L

# Проводим итерацию функции нахождения многочлена Лагранжа для одной точки
# по всему заданному интервалу функции с шагом 0,01
def lagranje(x, points_x, points_y):
    arr_y = []
    for i in x:
        arr_y.append(round(lagranje_point(i, points_x, points_y),2))
        # ROUND округляет значения до
        # двух знаков поле . (для удобства в консоли)
    return arr_y


X1 = -1.5  # X1 и X2 задают интервал, На котором строится функция
X2 = 1.5   # 
points = 15 # Points - количество узлов интерполяции


# рассчитываем координаты X узлов интерполяции из количества узлов
points_x = np.arange(X1,X2+0.000001, (abs(X1)+abs(X2))/points)
print(points_x)

# рассчитываем координаты Y узлов интерполяции
points_y = []
for i in points_x:
    points_y.append(round(np.tan(i),2)) #задаем интерполируемую функцию                 
print(points_y)

# x - координаты точек построения граффиков
x=np.arange(X1,X2+0.01,0.01)
# y - рассичтываем координаты y точек построения граффика по методу Лагранжа
y = lagranje(x, points_x, points_y)

# вывод граффика на печать
mpl.plot(x,np.tan(x)) # печать граффика функции
mpl.plot(x, y) # печать интерполяционного граффика
mpl.plot(points_x, points_y, 'go') # печпть узлов интерполяции
mpl.legend(['function', 'interpolation', 'base points']) # вывод легенды
mpl.show()
