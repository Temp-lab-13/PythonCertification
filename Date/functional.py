# Класс обработки основных команд.
from UI.bullderNote import buildNote, buildEdit
from Date.readLoader import load, save

# Добавление новой заметки


def add_note():
    global list_note
    list_note.append(buildNote(list_note))

# Показать текущий список заметок


def print_list(element=None):

    if element == None:
        for i in list_note:
            print('------------------------------')
            for item in i:
                print('{}{}'.format(item, i[item]))
            print('------------------------------')
    else:
        print('------------------------------')
        for item in element:
            print('{}{}'.format(item, element[item]))
        print('------------------------------')

# Найти запись по id


def get_note_ID(id):
    check = True
    for i in range(len(list_note)):
        if id == list_note[i]['ID: ']:
            check = False
            return list_note[i]
    if check:
        print('Заметка с указанным ID не найдена.')

# Найти запись по дате (выводит все записи за указанный день)


def get_note_Date(date):
    check = True
    for i in list_note:
        if date == i['Дата: ']:
            check = False
            print_list(i)
    if check:
        print('Заметок с указанной датой не найдено.')

# Редактирование существующей записи
# По сути перезаписывае заголовок, текст и обновляет дату.
# До реализации выбора редактирование элементов не успел добраться


def editing(id):
    element = get_note_ID(id)
    if id <= len(list_note):
        list_note[(id - 1)] = buildEdit(element)

# Удаляет запись целиком.


def delete(id):
    element = get_note_ID(id)
    print_list(element)
    list_note.remove(element)

# Загружает файл.
# Загрузка происходит жестко из специальной директории.
# Загрузка по умлчанию - файл save
# Но пользователь может выбрать загрузить свой файл,
# если он заранее был создан
# Думал сделать авто загрузку основного файла, но передумал.


def load_file(pathFile=0):
    global list_note
    tempDir = list()
    if pathFile == 0:
        tempDir = load('PythonCertification\Save\save.txt')
        if len(tempDir) != 0:
            list_note = tempDir
    else:
        tempDir = load(pathFile)
        if len(tempDir) != 0:
            list_note = tempDir

# Сохраняет данные в файл.
# Всё что верно для метода загрузки, валидно и для сохранения.


def save_file(pathFile=None):
    if pathFile == None:
        save('PythonCertification\Save\save.txt', list_note)
    else:
        save(pathFile, list_note)


# Глобальная кэш-переменная.
# В ней хранятся межсессион-записи.
list_note = list()
