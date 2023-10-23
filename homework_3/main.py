# 3. Создайте программу для игры в ""Крестики-нолики"".
from random import randint


def enter_number(message):  # ввести цифру с клавиатуры
    number = input(message)
    try:
        float(number)

    except ValueError:
        print("Введите число, попробуйте ещё раз!")
        return enter_number(message)
    return number


def switch(player):
    if player == 1:
        player = 0
        return player
    else:
        player = 1
        return player


def check_line(line1, line2, line3, player):
    l: list[str] = ["x", "o"]
    i = 1
    print_lines(line1, line2, line3)
    while i < 10:
        turn = int(enter_number(f"\nХодит игрок{player}.\n Введите число от 1 до 9:\n--> "))
        while turn < 1 or turn > 9:
            turn = int(enter_number(f"\nХодит игрок{player}.\n Введите число от 1 до 9:\n--> "))

        if turn == 7 and (line1[2] == "*"):
            line1[2] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 8 and (line1[4] == "*"):
            line1[4] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 9 and (line1[6] == "*"):
            line1[6] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 4 and (line2[2] == "*"):
            line2[2] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif (turn == 5) and (line2[4] == "*"):
            line2[4] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 6 and (line2[6] == "*"):
            line2[6] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 1 and (line3[2] == "*"):
            line3[2] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 2 and (line3[4] == "*"):
            line3[4] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        elif turn == 3 and (line3[6] == "*"):
            line3[6] = l[player]
            get_winner(line1, line2, line3, player)
            i += 1
            player = switch(player)
        else:
            print('\n!!!Сюда уже кто-то походил!!!\n!!!!Сделайте ход в другую клетку!!!!\n')

        print_lines(line1, line2, line3)

    return line1, line2, line3, player


def get_winner(line1, line2, line3, player):
    l: list[str] = ['x', 'o']

    for symbol in l:
        if ((line1[2] == symbol and line1[4] == symbol and line1[6] == symbol) or
                (line2[2] == symbol and line2[4] == symbol and line2[6] == symbol) or
                (line3[2] == symbol and line3[4] == symbol and line3[6] == symbol) or
                (line1[2] == symbol and line2[2] == symbol and line3[2] == symbol) or
                (line1[4] == symbol and line2[4] == symbol and line3[4] == symbol) or
                (line1[6] == symbol and line2[6] == symbol and line3[6] == symbol) or
                (line1[2] == symbol and line2[4] == symbol and line3[6] == symbol) or
                (line1[6] == symbol and line2[4] == symbol and line3[2] == symbol)):
            print_lines(line1, line2, line3)
            print(f">>>>>>>>>>Выиграл игрок {player}<<<<<<<<<<")
            exit()
    if line1.count("*") != 0 and line2.count("*") != 0 and line3.count("*") != 0:
        return line1, line2, line3, player
    else:
        print(">>>>>>>>>>Ничья, победила дружба<<<<<<<<<<")


def print_lines(line1, line2, line3):
    up_line = list("~_______~")
    down_line = list("~_______~")
    print(*up_line)
    print(*line1)
    print(*line2)
    print(*line3)
    print(*down_line)


def game():
    player = int(randint(0, 1))
    print("\nНачинаем игру в крестики-нолики!\n"
          "Для хода необходимо ввести цифру (как на NumLock), \nкоторая соответствует позиции на поле\n"
          "Цифры соответствуют таким позициям:")

    midl_line11 = list("| 7 8 9 |")
    midl_line22 = list("| 4 5 6 |")
    midl_line33 = list("| 1 2 3 |")

    print_lines(midl_line11, midl_line22, midl_line33)

    midl_line1 = list("| * * * |")  # 2.4.6
    midl_line2 = list("| * * * |")
    midl_line3 = list("| * * * |")
    check_line(midl_line1, midl_line2, midl_line3, player)

game()
