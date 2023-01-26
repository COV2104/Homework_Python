# Вычислить значение выражения:
# 12 + 15
# 12 / 15
# 112 * 15


# 1. Где операторы?
# 2. Где числовые значения?

def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        if c != 0:
            return a / b
        else:
            print("Деление на ноль!")
    elif ch == '*':
        return a * b

# Уровень 1:

# - 1 действие
# - 2 аргумента


example_1 = '25 + 25'
print(example_1)
n = example_1.split(' ')
a, b, c = n[0], n[2], n[1]


def calc_1(a, b, c):
    if c == '+':
        print(int(a) + int(b))
    elif c == '-':
        print(int(a) - int(b))
    elif c == '*':
        print(int(a) * int(b))
    elif c == '/':
        if c != 0:
            print(int(a) / int(b))
        else:
            print("Деление на ноль!")


calc_1(a, b, c)

# Уровень 2:

# - Количество действие произвольное
# 12 + 15 - 4

example_2 = '25 + 25 - 10 + 40 + 20'
print(example_2)


def calc_2(text):
    n = text.split(' ')
    temp = n[0]
    for i in range(len(n)):
        if i % 2 != 0:
            if n[i] == '+':
                temp = (int(temp) + int(n[i+1]))
            elif n[i] == '-':
                temp = (int(temp) - int(n[i+1]))
            elif n[i] == '*':
                temp = (int(temp) * int(n[i+1]))
            elif n[i] == '/':
                if n[i+1] != 0:
                    temp = (int(temp) / int(n[i+1]))
                else:
                    print("Деление на ноль!")
    print(temp)


calc_2(example_2)

# Уровень 3:

# - Действия имеют приоритет
# 12 - 4 * 2

example_3 = '200 / 10 + 63 - 10 + 100 * 2 * 10 - 15'


def line_calculation(text):
    m = text.split()
    m_2 = []
    result = int(m[0])
    for i in range(1, len(m), 2):
        if m[i] == '+' or m[i] == '-':
            result = int(m[i+1])
        if m[i] == '*' or m[i] == '/':
            result = calc(result, int(m[i + 1]), m[i])
            if len(m_2) > 1:
                m_2.pop()
            m_2.append(result)
        else:
            m_2.append(m[i])
            m_2.append(int(m[i+1]))
    if m[1] == '+' or m[1] == '-':
        m_2.insert(0, int(m[0]))
    res = m_2[0]
    if len(m_2) > 2:
        for i in range(1, len(m_2) - 1, 2):
            res = calc(res, int(m_2[i + 1]), m_2[i])
    else:
        res = m_2[-1]
    return res


print(example_3)
print(line_calculation(example_3))

# Уровень 4:
# - Действия разделяются скобками

# (12 - 4) * 2
