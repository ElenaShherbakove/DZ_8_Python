# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
#  Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных
# Простой вариант:
# Пронумеровать контакты и выбрать изменяемый по номеру.

def view(name):
    with open(name, 'r', encoding='utf-8') as book:
        print(book.read(), end='')


def add(name):
    with open(name, 'a', encoding='utf-8') as book:
        name = input('Введите ФИО ')
        number = input('Введите номер телефона ')
        book.write(f"{name} : {number}")
        print(f'Запись {name} {number} добавлена')


def search(name):
    result = []
    search_str = input('Введите ФИО или номер телефона для поиска ')
    with open(name, 'r', encoding='utf-8') as book:
        number_book = book.read().split('\n')
    for line in number_book:
        if search_str in line:
            result.append(line)
    return result


# def edit(name):
#
#
# def deleted(name):



phone_book = 'phone_book.txt'

with open(phone_book, 'a', encoding='utf-8') as file:
    file.write('')

while True:

    choice = input('Выберите действие\n1-просмотр, 2-добавление, 3-поиск, 4-редактирование, 5-удаление, 6-выход\n=> ')

    if choice == '1':
        view(phone_book)
    elif choice == '2':
        add(phone_book)
    elif choice == '3':
        search(phone_book)
    elif choice == '4':
        ...
    elif choice == '5':
        ...
    else:
        ...
    break