# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

import os
from datetime import time


def clear_screen():
    os.system('cls')


def search_data():
    clear_screen()
    while (True):
        answer = input('Строка поиска(для выхода нажмите Enter)=>')
        if answer == '':
            return
        result = []
        with open('phones.txt', 'r', encoding='utf-8') as datafile:
            for line in datafile:
                result.append(line.strip('\n'))
                result = list(filter(lambda line: answer in line, result))
        for printdata in result:
            output_data_string(printdata)


def output_data_string(printdata):
    parse_data = printdata.split(',')
    print(f'{parse_data[0]}  {parse_data[1]}  {parse_data[2]}   {parse_data[3]}')

def save_data_to_file(data_to_save):
    data_to_save = ','.join(data_to_save) + '\n'
    print(data_to_save)
    with open('phones.txt', 'a', encoding='utf-8') as datafile:
        datafile.write(data_to_save)


def print_data():
    count = 1
    with open('phones.txt', 'r', encoding='utf-8') as datafile:
        for line in datafile:
            parse_data = line.replace("\n", "").split(',')
            print(f'{count}: {parse_data[0]}  {parse_data[1]}  {parse_data[2]}   {parse_data[3]}')
            count += 1
    return count-1


def data_export():
    count = print_data()
    input(f'Всего {count} записей. Enter для выхода. ')


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
        save_data_to_file(data_to_save)


def data_dell():
    while (True):
        answer = input('Введите параметр удаления полностью(для выхода нажмите Enter)=> ')
        if answer == '':
            return
        result = []
        temp = []
        with open('phones.txt', 'r', encoding='utf-8') as datafile:
            for line in datafile:
                result.append(line.strip('\n'))
                if answer in line:
                    temp.append(line.strip('\n'))
            if len(temp) == 1:
                delete = "".join(temp)
            else:
                print('Найдено несколько контактов с данными параметрами:')
                count = 1
                for item in temp:
                    print(f'{count}: {item}')
                    count+=1
                num = int(input('Введите номер контакта который необходимо удалить: '))    
                for i in range(len(temp)):
                    if i == num-1:
                        delete = "".join(temp[i])
        new = []
        for line in result:
            if line != delete:
                new.append(line)       
        with open('phones.txt', 'w', encoding='utf-8') as datafile:
            for i in new:
                datafile.write(i+'\n')


if __name__ == '__main__':
    menu = '''1 - Вывод данных\n2 - Добавление записи\n3 - Поиск\n4 - Удаление данных\n5- Выход'''
    while (True):
        os.system("cls")
        print(menu)
        answer = input('>:')
        match answer:
            case "1":
                # вывод данных
                data_export()

            case "2":
                # добавление данных
                data_import()

            case "3":
                # поиск
                search_data()

            case "4":
                # удаление данных
                data_dell()

            case "5":
                # выход
                exit(0)

            case _:
                print("неверный ввод")
                time.sleep(3)



