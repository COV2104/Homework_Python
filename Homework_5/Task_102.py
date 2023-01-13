# Задача 102 Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


n = int(input('Введите число: '))
divider = 2
factor = []
while divider*divider <= n:
    if n % divider == 0:
        factor.append(divider)
        n //= divider
    else:
        divider += 1
if n > 1:
    factor.append(n)

print(factor)
