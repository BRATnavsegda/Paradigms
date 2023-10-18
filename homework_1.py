# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers: list[int]):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]


# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
def sort_list_declarative(numbers: list[int]):
    numbers.sort(reverse=True)


if __name__ == '__main__':
    lst_1 = [2, 3, 1, 4, 5]
    sort_list_imperative(lst_1)
    print(lst_1)
    lst_2 = [2, 3, 1, 4, 5]
    sort_list_declarative(lst_2)
    print(lst_2)
