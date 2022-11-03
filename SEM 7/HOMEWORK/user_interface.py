
def get_data():
    data = []
    surname = input('Введите фамилию: ')
    data.append(surname)
    name = input('Введите имя: ')
    data.append(name)
    phone_number = input('Введите номер телефона: ')
    if phone_number.isdigit():
        data.append(phone_number)
    else:
        phone_number = input('Номер телефона может состоять только из цифр! Введите номер телефона: ')
        data.append(phone_number)
    description = input('Введите описание: ')
    data.append(description)
    return data