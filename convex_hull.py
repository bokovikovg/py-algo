import matplotlib.pyplot as plt # подключение модуля pyplot библиотеки matplotlib для отрисовки точек и оболочки

def convex_hull(points):

    """
        Алгоритм для нахождения минимальной выпуклой оболочки множества точек
        На вход получаем список точек х, у на плоскости (то есть [(x1, y1), (x2, y2) ...])
        (x, y) -- кортеж
        Сортируем наш список по х координате
        Инициализируем upper и lower как пустые списки, они будут
            содержать точки верхней и нижней половин оболочки соответственно

        цикл фор по все точкам от первой до последней:
            пока lower содержит хотя бы 2 точки и
                последовательность последних двух последних точек в lower и точки p
                    не дает поворот против часовой стрелки
                        (векторное произведение двух векторов построенных из 2х точек <= 0):
                            удаляем последнюю точку из lower
                добавляем точку р в lower

        для upper то же самое только идем по точкам с конца

        возвращаем объединение upper и lower (развернутых)
    """
    points = sorted(set(points))

    if len(points) <= 1:
        return points

    # cross product of OA and OB
    # returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.

    def cross(o, a, b):
        return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    upper = []

    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]
# функция для отрисовки оболочки
def draw_hull(points):
    hull = convex_hull(points) # получаем оболочку
    fig, ax = plt.subplots() # создаем фигуру, на которой будем рисовать
    x, y = zip(*points) # разворачиваем points на отдельные списки х и у
    #print(x, y)
    plt.scatter(x, y) # отмечаем точки на плоскости
    hull.append(hull[0])
    x, y = zip(*hull) # получаем списки х и у точек оболочек
    plt.plot(x, y) # создаем график
    plt.show() # рисуем

    """
        вызов:
         convex_hull([(x1, x2), (x2, y2), (x3, y3), (x4, y4) .. etc])
         такой же вызов для функции которая еще рисует draw_hull(-//-)
