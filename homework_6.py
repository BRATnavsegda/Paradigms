# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.
from random import randint


# from bisect import bisect_left
#
# # Константа для поиска индекса
# CONSTANT = 4
#
# # Задаем массив
# array = [1, 2, 3, 5, 8, 4]
#
# # Сортируем
# array.sort()
#
# # Выводим отсортированный массив
# print(array)
#
# def binary_search(array, target):
#     # Поиск индекса искомого элемента
#     result = bisect_left(array, target)
#     if result == len(array):
#         return -1
#     else:
#         return result
#
#
# # Поиск индекса искомого элемента
# print(binary_search(array, CONSTANT))

# Хотел написать в декларативном стиле, после подгона под условия задачи, уже и не уверен, что еще декларативный. :)


# Вариант 2 ____________________________________________________________________________________________________


def binary_search(array, target):
    """
        Функция выполняет бинарный поиск по отсортированному массиву для нахождения индекса целевого значения.
        Параметры:
            array (List): Отсортированный список целых чисел.
            target (int): Значение, которое необходимо найти в массиве.
        Возвращает:
            int: Индекс целевого значения в массиве, или -1, если значение не найдено.

        >>> binary_search([1, 2, 3, 5, 8, 4], 5)
        3
        >>> binary_search([1, 2, 3, 5, 8, 4], 6)
        -1
        """
    if len(array) == 0:
        return -1
    elif len(array) == 1:
        if array[0] == target:
            return target
        else:
            return -1

    first_half = 0
    second_half = len(array) - 1
    while first_half <= second_half:
        middle = (first_half + second_half) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            first_half = middle + 1
        else:
            second_half = middle - 1
    return -1


if __name__ == '__main__':
    test_array = [i for i in range(100)]

    print(test_array)
    print(binary_search(test_array, 55))
