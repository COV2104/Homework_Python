# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

import os
from datetime import time

file = 'D:\Домашка Олеся\Homework_Python\Homework_6\phones.txt'

def clear_screen():
    os.system('cls')

def file_open(file):
    result = []
    with open(file, 'r', encoding='utf-8') as datafile:
            for line in datafile:
                result.append(line.strip('\n'))
    return result             

def data_import():
    while (True):
        print('Добавление записи(для выхода нажмите Enter)')
        last_name = input('Фамилия: ')
        first_name = input('Имя: ')
        patronymic = input('Отчество: ')
        phone_number = input('Телефон: ')
        data_to_save = [last_name, first_name, patronymic, phone_number]
        if '' in data_to_save:
            return
        data_to_save = ','.join(data_to_save)    
        save(file,data_to_save)

def save(file,data_to_save):
    with open(file, 'a', encoding='utf-8') as datafile:
        datafile.write(data_to_save + '\n')

def data_export(file):
    count = 1
    with open(file, 'r', encoding='utf-8') as datafile:
        for line in datafile:
            parse_data = line.replace("\n", "").split(',')
            print(f'{count}: {parse_data[0]}  {parse_data[1]}  {parse_data[2]}   {parse_data[3]}')
            count+=1
    input(f'Всего {count} записей. Enter для выхода. ')        

def search(file):
    while (True):
        answer = input('Введите параметр поиска(для выхода нажмите Enter)=> ')
        if answer == '':
            return
        result = []
        temp = []
        with open(file, 'r', encoding='utf-8') as datafile:
            for line in datafile:
                result.append(line.strip('\n'))
                if answer.lower() in line.lower():
                    temp.append(line.strip('\n'))
                 
            if len(temp) == 1:
                quest = "".join(temp)
            elif len(temp) == 0:
                print('Данные не найдены') 
                continue   
            else:
                print('Найдено несколько контактов с данными параметрами:')
                count = 1
                for item in temp:
                    print(f'{count}: {item}')
                    count+=1  
                num = int(input('Введите номер контакта который необходим: ')) 
                for i in range(len(temp)):
                    if i == num-1:
                        quest = "".join(temp[i]) 
        return quest                       

def data_seach(file):
    while(True):
        print(search(file))
        answer = input('(Enter)=> ')
        if answer == '':
            return
        
def dell(result,delete):
    new = []
    for line in result:
        if line != delete:
            new.append(line)
    with open(file, 'w', encoding='utf-8') as datafile:
        for i in new:
            datafile.write(i+'\n')

def data_dell(file):
    result = file_open(file)
    delete = search(file)
    dell(result,delete)               

def data_change(file):
    change1 = ''.join(search(file)).split(',')
    change = ','.join(change1)
    dell(file_open(file),change)
    print(f'{change1[0]} {change1[1]} {change1[2]} {change1[3]}')
    phone = input('Введите новый номер телефона: ')
    change1[3] = phone
    temp = ','.join(change1)
    save(file,temp)
    

if __name__ == '__main__':
    menu = '''1 - Показать все записи\n2 - Добавить новый контакт\n3 - Найти запись\n4 - Удалить контакт\n5 - Изменить номер телефона у контакта\n6 - Выход'''
    while (True):
        os.system("cls")
        print(menu)
        answer = input('=> ')
        match answer:
            case "1":
                # вывод данных
                data_export(file)

            case "2":
                # добавление данных
                data_import()

            case "3":
                # поиск
                data_seach(file)

            case "4":
                # удаление данных
                data_dell(file)

            case "5":
                # Изменить номер телефона у контакта
                data_change(file)

            case "6":
                # выход
                exit(0)

            case _:
                print("неверный ввод")
                time.sleep(3)


