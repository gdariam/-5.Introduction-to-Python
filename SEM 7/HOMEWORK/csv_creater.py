from user_interface import get_data as gd

def create():
    file = 'Phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')

data_pb = gd()
def writing_csv():
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{data_pb[0]};{data_pb[1]};{data_pb[2]};{data_pb[3]}\n')