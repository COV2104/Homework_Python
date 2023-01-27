# Вычислить значение выражения:
# 12 + 15
# 12 / 15
# 112 * 15


# 1. Где операторы?
# 2. Где числовые значения?

# Уровень 1:

# - 1 действие
# - 2 аргумента


# Уровень 2:

# - Количество действие произвольное
# 12 + 15 - 4


# Уровень 3:

# - Действия имеют приоритет
# 12 - 4 * 2

example_3 = '200 / 10 + 63 - 10 + 100 * 2 * 10 '

def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        if ch != 0:
            return a / b
        else:
            print("Деление на ноль!")
    elif ch == '*':
        return a * b

def calculator(text):
    prioritet = {'+': 1, '-': 1, '*': 2, '/': 2}
    m = text.split(' ')
    numbers = []
    operation = []
    for i in range(len(m)-1):
        if m[i].isdigit() and m[i-1] != '*' and m[i-1] != '/':
            numbers.append(m[i])
        elif m[i] in prioritet:
            if  m[i] == '+' or m[i] == '-' :
                operation.append(m[i])
            elif  m[i] == '*' or m[i] == '/' :   
                a = int(numbers.pop(-1))
                b = int(m[i+1])
                ch = m[i]
                res = calc(a, b, ch)
                numbers.append(res)
    res = int(numbers[0])  
    i = 0
    while i < len(numbers)-1:
        a = res
        b = int(numbers[i+1])
        ch = operation[i]
        res = calc(a, b, ch)  
        i+=1
    
    
    print(numbers)
    print(operation)  
    print(res)           


print(example_3)
calculator(example_3)

# Уровень 4:
# - Действия разделяются скобками

# (12 - 4) * 2