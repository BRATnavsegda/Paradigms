# Таблица умножения
# Домашнее задание
# ● Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# ● Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9

def multiply_table(column_number: int) -> list[list[str]]:
    """
    Generates a multiplication table up to the specified column number.

    Args:
        column_number (int): The number of columns in the multiplication table.

    Returns:
        list[list[str]]: A nested list of strings representing the multiplication table.

    Examples:
        >>> multiply_table(3)[2][1]
        '3 * 1 = 3\\n'
    """

    result_list = []
    for column in range(1, column_number + 1):
        row_list = ['\n']
        for row in range(1, 11):
            row_list.append(f"{column} * {row} = {column * row}\n")
        result_list.append(row_list)
    return result_list


# Здесь используются императивный, структурный и процедурный стили,
# потому что они наиболее подходят для поставленной задачи.


if __name__ == '__main__':

    print(*multiply_table(3)[2])

    for item in multiply_table(3):
        print(*item, end='')
