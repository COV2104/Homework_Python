# Задача 106 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)
from random import randint


def players_choice(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def bot_choice(candy):
    k = randint(1, 28)
    if candy < 58:
        k = candy - 29
        if k == 0:
            k = 1
    return k


player_1 = input("Введите имя игрока: ")
player_2 = "Bot"
candy = int(input("Введите количество конфет на столе: "))
draw = randint(0, 1)
if draw:
    print(f"Первый ходит {player_1}")
else:
    print(f"Первый ходит {player_2}")

candies_1 = 0
candies_2 = 0

while candy > 28:
    if draw:
        k = players_choice(player_1)
        candies_1 += k
        candy -= k
        draw = False
        print(f"Ходил {player_1}, он взял {k}, теперь у него {candies_1}. На столе осталось {candy} конфет.")
    else:
        k = bot_choice(candy)
        candies_2 += k
        candy -= k
        draw = True
        print(f"Ходил {player_2}, он взял {k}, теперь у него {candies_2}. На столе осталось {candy} конфет.")

if draw:
    print(f"Выиграл {player_1}")
else:
    print(f"Выиграл {player_2}")
