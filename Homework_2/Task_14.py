# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def powers_of_two(n):
    i=2
    k=1
    numbers=[]
    while i**k <= n:
        number = i**k
        numbers.append(number)
        k+=1
    return numbers    

try:
    n = int(input('Введите число: '))
    print(powers_of_two(n))
except:
    print('Некорректный ввод. Попробуйте еще раз!')    
