# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input('Введите трехзначное число: ')
if len(number) == 3:
    number = int(number)
    num_1 = number//100
    num_2 = int(number/10) % 10
    num_3 = number % 10
    summa = num_1+num_2+num_3
    print(f'Сумму цифр трехзначного числа = {summa}')
else:
    print('Error:Введите трехзначное число')
    
