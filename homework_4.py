# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.


from math import sqrt

array_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def my_function(x, y):
    len_x = len(x)
    if len(y) != len_x:
        raise ValueError('both arrays must have same number of data points')
    if len_x < 2:
        raise ValueError('arrays must have at least two data points')
    x_average = sum(x) / len_x
    y_average = sum(y) / len_x
    sxy = sum((xi - x_average) * (yi - y_average) for xi, yi in zip(x, y))
    sxx = sum((xi - x_average) ** 2.0 for xi in x)
    syy = sum((yi - y_average) ** 2.0 for yi in y)
    try:
        return sxy / sqrt(sxx * syy)
    except ZeroDivisionError:
        raise ValueError('at least one of arrays is constant')


print(my_function(array_1, array_2))
