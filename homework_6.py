# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.

from bisect import bisect_left

# Константа для поиска индекса
CONSTANT = 4

# Задаем массив
array = [1, 2, 3, 5, 8, 4]

# Сортируем
array.sort()

# Выводим отсортированный массив
print(array)

def binary_search(array, target):
    # Поиск индекса искомого элемента
    result = bisect_left(array, target)
    if result == len(array):
        return -1
    else:
        return result


# Поиск индекса искомого элемента
print(binary_search(array, CONSTANT))

# Хотел написать в декларативном стиле, после подгона под условия задачи, уже и не уверен, что еще декларативный. :)

