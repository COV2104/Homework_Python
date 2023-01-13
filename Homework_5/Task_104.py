# Задача 104. Даны два файла file1.txt и file2.txt, в каждом из которых находится
# запись многочлена (полученные в результате работы программы из задачи 103).
# Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.

def selection_coefficients(string):
    s = string
    l = len(s)
    numbers = []
    i = 0
    while i < l:
        s_int = ''
        a = s[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = s[i]
            else:
                break
        i += 1
        if s_int != '':
            numbers.append(int(s_int))
    coefficient = []
    for i in range(len(numbers)-2):
        if i % 2 == 0:
            coefficient.append(numbers[i])
    coefficient.append(numbers[-2])
    return coefficient


def sum_of_polynomials(pol1,pol2):
    if len(pol1) > len(pol2):
        while len(pol1) != len(pol2):
            pol2.insert(0,0)
    else:
        while len(pol1) != len(pol2):
            pol1.insert(0,0)        
    pol_sum = []
    for i in range(len(pol1)):
        sum = pol1[i] + pol2[i]
        pol_sum.append(sum)
    k=len(pol_sum)
    polynomial = ''
    if len(pol_sum) == 1:
        polynomial = str(pol_sum[0])
    for i in range(len(pol_sum)):
        if i < len(pol_sum)-2:
            polynomial += f'{pol_sum[i]}*x^{k-1} + '
        elif i == len(pol_sum)-2:
            polynomial += f'{pol_sum[i]}*x + '    
        elif i == len(pol_sum)-1:
            polynomial += f'{pol_sum[i]} = 0' 
        k-=1    
    return polynomial       

def open_file(file):
    with open(f'{file}', 'r') as data:
        pol = data.read()
    return pol
      
def write_file(pol1,pol2):
    with open('file_sum.txt','w') as file:
        file.write(sum_of_polynomials(pol1,pol2))


file_1 = selection_coefficients(open_file('file1.txt'))
file_2 = selection_coefficients(open_file('file2.txt'))
write_file(file_1,file_2)

