# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def stepen(a, b):
    if b == 0:
        return 1
    return a * stepen(a, b-1)


try:
    a = int(input('Введите число: '))
    b = int(input('Введите степень: '))
    print(f"{a} ^ {b} = {stepen(a,b)}")
except:
    print('Некорректный ввод. Попробуйте еще раз!')