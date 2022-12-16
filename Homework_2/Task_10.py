# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2
import random

def flip_a_coin(n):
    coins = []
    count_0 = 0
    count_1 = 0
    for i in range(0, n):
        coin = random.randint(0, 1)
        coins.append(coin)
        if coins[i] == 0:
            count_0 += 1
        elif coins[i] == 1:
            count_1 += 1
    print(coins)
    if count_0 > count_1:
        return count_1
    else:
        return count_0


try:
    n = int(input('Введите количество монеток: '))
    print(f'Необходимо перевернуть минимум: {flip_a_coin(n)}')
except:
    print('Некорректный ввод. Попробуйте еще раз!')
