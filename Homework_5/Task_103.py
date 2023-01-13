# Задача 103 Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.

# Пример:  k=2

# Возможные варианты многочленов:
# 2*x*x + 4*x + 5 = 0
# x*x + 5 = 0
# 10*x*x = 0

import random

def creating_polynomial(k):
    odds = [(random.randint(0, 100)) for i in range(k+1)]
    polynomial = ''
    if len(odds) == 1:
        polynomial = str(odds[0])
    for i in range(k, -1, -1):
        if i > 1:
            polynomial += f'{odds[i]}*x^{i} + '
        elif i == 1:
            polynomial += f'{odds[i]}*x + '    
        elif i < 1:
            polynomial += f'{odds[i]} = 0'    
            
    return polynomial

def write_file(k):
    with open('file2.txt','w') as file:
        file.write(creating_polynomial(k))

k = int(input('Введите степень многочлена: '))  
write_file(k)  