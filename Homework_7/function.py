bus_txt = 'bus.txt'
driver_txt = 'driver.txt'
bus_route_txt = 'bus_route.txt'

def print_bus():
    print('|id\t|марка ТС\t|гос. номер\t|')
    print('-'*41)
    with open(bus_txt, 'r', encoding='utf-8') as datafile:
        for line in datafile:
            parse_data = line.replace("\n", "").split(',')
            print(f'|{parse_data[0]}\t|{parse_data[1]}\t|{parse_data[2]}\t|')
    input(f'Enter > ') 

def print_driver():
    print('|id\t|Фамилия\t|Имя\t|Отчество\t|номер телефона\t|стаж работы\t|')
    print('-'*81)
    with open(driver_txt, 'r', encoding='utf-8') as datafile:
        for line in datafile:
            parse_data = line.replace("\n", "").split(',')
            print(f'|{parse_data[0]}\t|{parse_data[1]} {parse_data[2]} {parse_data[3]} {parse_data[4]} {parse_data[5]}')
    input(f'Enter > ') 
        

def print_route():        
    routes = read_data_from_file(bus_route_txt)
    buses = read_data_from_file(bus_txt)
    drivers = read_data_from_file(driver_txt)
    print('| номер маршрута | ст. отправления | ст. назначения | интервал движения | гос.номер ТС | ФИО водителя |')
    print('-'*103)
    for r_name,r_start,r_end,interval,r_bus,r_driver in routes:
        for id_record,item_1,item_2 in buses:
            if r_bus==id_record:
                bus_number = item_2
        for id_record,item_1,item_2,item_3,item_4,item_5 in drivers:
            if r_driver==id_record:
                fio = item_1,item_2,item_3
                driver_name = ' '.join(fio)
        print(f'|{r_name}\t| {r_start} - {r_end}   {interval}   {bus_number}   {driver_name}')
    input(f'Enter > ') 
    

def add_bus():
    print('Добавление транспортного средства: ')
    id_bus = input('id транспортного средства: ')
    vehicle_brand = input('марка ТС: ')
    state_number = input('гос. номер: ')
    data_to_save = [id_bus, vehicle_brand, state_number]
    data_to_save = ','.join(data_to_save)    
    save(bus_txt,data_to_save)

def add_driver():
    print('Добавление водителя: ')
    id_driver = input('id водителя: ')
    last_name = input('Фамилия: ')
    first_name = input('Имя: ')
    patronymic = input('Отчество: ')
    phone_number = input('Телефон: ')
    work_experience = input('Стаж работы: ')
    data_to_save = [id_driver, last_name, first_name, patronymic, phone_number, work_experience]
    data_to_save = ','.join(data_to_save)    
    save(driver_txt,data_to_save)             

def add_route():
    print('Добавлениу маршрута: ')
    number_route = input('номер маршрута: ')
    start = input('станция отрпавления: ')
    end = input('станция назначения: ')
    interval = input('интервал движения: ')
    id_ts = input('id транспортного средства: ')
    id_driver = input('id водителя: ')
    data_to_save = [number_route,start,end,interval,id_ts,id_driver]
    data_to_save = ','.join(data_to_save)    
    save(bus_route_txt,data_to_save)   

def save(file,data_to_save):
    with open(file, 'a', encoding='utf-8') as datafile:
        datafile.write(data_to_save + '\n') 
    input('Запись добавлена. Enter >')  

def read_data_from_file(name):
    rawdata_list = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            rawdata_list.append(line.strip('\n').split(','))
        return rawdata_list           