# Задача 101 Вычислить число π c заданной точностью d

# Пример:
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001
import math

# 1 вариант :

def rounds(num, max=2):
    left, right = str(num).split('.')
    zero, nums = zero_nums = [], []
    for n in right:
        zero_nums[0 if not nums and n == '0' else 1].append(n)
        if len(nums) == max:
            break
    return '.'.join([left, ''.join(zero) + ''.join(nums)])

d = int(input('Введите необходимое количество знаков после запятой для числа Пи: '))
n = 1
number_pi = 0
for n in range(1, 1000000):
    number_pi = number_pi+4*((-1)**(n+1))/(2*n-1)
print(rounds(number_pi, d))

# 2 вариант:

number_pi = str(math.pi)
d = int(len(input('Задайте точность выводимого числа Пи в диапазоне от 0.0000000001 до 0.1: ')))
number_pi = ('').join(number_pi[:d])
print(number_pi)