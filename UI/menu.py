# Методы обрботки работы меню.
##############################
from Date.functional import *
from datetime import datetime


# Метод печати списка команд меню.
def print_menu():
    print('Меню: ')
    print(' 1 - создать новую запись;',
          ' 2 - показать список;',
          ' 3 - выбарть запись;',
          ' 4 - выбрать дате по дате создания;',
          ' 5 - редактировать запись;',
          ' 6 - удалить запись;',
          ' 7 - сохранить в основной файл;',
          ' 8 - сохранить в другой файл;',
          ' 9 - загрузить из основного файла;',
          ' 10 - загрузить из другого файла;',
          ' 11 - завершить рабту.\n', sep='\n')


# Метод выбора команды в меню и её запуск.
def choice_in_menu():
    flag = True
    while flag:
        print_menu()
        try:
            enter = int(input('Введите номер команды: '))
            match enter:
                case 1: add_note()
                case 2: print_list()
                case 3: print_list(get_note_ID(input_ID()))
                case 4: get_note_Date(input_Date())
                case 5: editing(input_ID())
                case 6: delete(input_ID())
                case 7: save_file()
                case 8: save_file(input_path())
                case 9: load_file()
                case 10: load_file(input_path())
                case 11: flag = False
        except ValueError:
            print('ERROR: Не корректная команда!\n')

# Обработка ввода ID


def input_ID():
    try:
        return int(input('Введите ID заметки: '))
    except Exception:
        print('Ошибка! Введён не корректный ID')

# Обработка ввода Даты


def input_Date():
    try:
        date = input(
            'Введите Дату создания заметки/последнего изменения заметки(2023-12-27): ')
        date = datetime.strptime(date, "%Y-%m-%d")
        date = date.strftime("%Y-%m-%d")
        return date
    except Exception:
        print('Ошибка! Введён не корректная Дата')


'''
Собирает путь для загрузки/сохраниния.
У пользователя нет доступа к тому что бы сменить директорию
для хранения записей, но он может создать несколько списков
своих заметок. 
'''


def input_path():
    pathFile = 'PythonCertification/Save/'
    pathFile = pathFile + input('Введите название списка: ')
    pathFile = pathFile + '.txt'
    return pathFile
