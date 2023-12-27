# Класс для работы с файлами.
import os
import json

# Загружает списки флормата json


def load(path):
    try:
        with open(path, encoding='utf-8') as data:
            return json.load(data)
    except FileNotFoundError:
        print('Файл не найден или не доступен.')


'''
Методы сохранения списока в файл в формате Json
save - чек-метод, проверяет существование одноимённого файла,
если true то запускает rec_file, 
'''


def save(pathFile, list_note):
    if os.path.isfile(pathFile):
        if rec_file():
            true_save(pathFile, list_note)
    else:
        true_save(pathFile, list_note)

# Сохраняет список в файл


def true_save(path, list_note):
    try:
        with open(path, 'w', encoding='utf-8') as data:
            data.write(json.dumps(list_note, ensure_ascii=False))
    except Exception:
        print('Ошибка записи!')

# Эта фигня должна была быть в файле menu,
# но возникла какая-то непонятная проблема с импортом из него.
# По этому оставил здесь.
# Запрашивает у пользователя подтверждение перезаписи файла.


def rec_file():
    print('Перезаписать существующий файл?')
    enter = input('Y - да | N - нет: ').lower()
    if enter == 'y':
        return True
    elif enter == 'n':
        return False
    else:
        print('Введена не коректная команда. Сброс.')
        return False
