# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12
import random

n = int(input('Введите кол-во элементов первого набора: '))
m = int(input('Введите кол-во элементов второго набора: '))

first_list = [(random.randint(-20, 20)) for i in range(n)]
print(first_list)
second_list = [(random.randint(-20, 20)) for i in range(m)]
print(second_list)

#  1 вариант

result = sorted(list(set(first_list) & set(second_list)))
if len(result) < 1:
    print('Общих элементов в данных наборах нет')
else:
    print(result)

#  2 вариант

result = []
for item in set(first_list):
    if item in set(second_list):
        result.append(item)

for i in range(len(result)-1):
    for j in range(len(result)-i-1):
        if result[j] > result[j+1]:
            result[j], result[j+1] = result[j+1], result[j]

if len(result) < 1:
    print('Общих элементов в данных наборах нет')
else:
    print(result)
