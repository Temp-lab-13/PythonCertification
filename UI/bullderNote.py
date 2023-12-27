# Класс-сборщик
from datetime import datetime

# Собирает новую запись


def buildNote(list_note):

    new_dict = dict()

    if len(list_note) != 0:
        new_dict['ID: '] = (list_note[-1]['ID: ']) + 1
    else:
        new_dict['ID: '] = 1
    new_dict['Дата: '] = datetime.now().strftime("%Y-%m-%d")
    new_dict['Название: '] = enter_top()
    new_dict[''] = enter_text()
    list_note = new_dict
    return list_note

# Пересобирает редактируемую запись.


def buildEdit(dict):
    dict['Дата: '] = datetime.now().strftime("%Y-%m-%d")
    dict['Название: '] = enter_top()
    dict[''] = enter_text()
    return dict

# Обработка ввода заголовка.


def enter_top():
    try:
        return input('Введите заголовок заметки: ')
    except Exeption:
        print('Ошибка!')

# Обработка ввода текста-тела заметки


def enter_text():
    try:
        print('Введите текст заметки: ')
        return input()
    except Exeption:
        print('Ошибка!')
