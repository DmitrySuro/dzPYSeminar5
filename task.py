# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга. Первый ход
# определяется жеребьёвкой. За один ход можно
#  забрать не более чем 28 конфет. Все конфеты оппонента
# достаются сделавшему последний ход. Сколько конфет нужно
#  взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

def win_game(first_player, second_player, total_sweets):
    who_turn = lottery_turn
    while total_sweets > 0:
        if who_turn == first_player:
            total_sweets = total_sweets - \
                int(input(f'Ваш ход старина {first_player}: '))
            who_turn = second_player
        else:
            total_sweets = total_sweets - \
                int(input(f'Ваш ход старина {second_player}: '))
            who_turn = first_player
    if who_turn == first_player:
        who_turn = second_player
    else:
        who_turn = first_player
    return who_turn


def lottery_turn(first_player, second_player, who_turn):
    lot_first_player = int(input(f'{first_player} введите любое число - '))
    lot_second_player = int(
        input(f'Теперь вы {second_player} введите число - '))
    if lot_first_player != lot_second_player:
        if lot_first_player > lot_first_player:
            who_turn = first_player
        else:
            who_turn = second_player
    return who_turn


first_player = input('Введите ваше имя: ')
second_player = input('Введите ваше имя: ')
total_sweets = 2021

print(win_game(first_player, second_player, total_sweets))
