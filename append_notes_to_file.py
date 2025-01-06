# grade 1. Этап 4. Задание 4

import copy
from datetime import date, datetime

def create_note(titles_stat={}):
    temp_for_title = 1
    while True:
        asker = input('Вы хотите добавить новую заметку? Да/Нет ').capitalize()
        if asker == 'Да':                  # Создание заметки
            username = input('Введите имя пользователя: ').capitalize()
            title = input('Введите заголовок заметки: ').capitalize()
            content = input('Введите описание заметки: ').capitalize()
            current_date = str(date.today())
            while True:
                status = input('Введите статус заметки (Новая, В процессе, Выполнено): ').capitalize()
                if status == 'Новая' or status == 'В процессе' or status == 'Выполнено':
                    break
                else:
                    print('Вы ввели некоректный статус заметки! ')
            while True:
                issue_date = input('Введите нужную дату в формате ЧЧ.ММ.ГГГГ: ')
                format = "%d.%m.%Y"
                try:
                    res = bool(datetime.strptime(issue_date, format))
                    break
                except ValueError:
                    print('Вы ввели некоректный формат даты!')
            titles_stat[f'Заметка {temp_for_title}'] = {
                'Имя пользователя':  username ,
                'Заголовок заметки': title,
                'Описание заметки': content,
                'Статус заметки': status,
                'Текущая дата': current_date,
                'Дата дедлайна': issue_date
            }
            temp_f = titles_stat[f'Заметка {temp_for_title}']
            print('-------------------------')
            print(f'Введенная заметка:',
                  '\nИмя пользователя:', temp_f['Имя пользователя'],
                  '\nЗаголовок заметки:', temp_f['Заголовок заметки'],
                  '\nОписание заметки:', temp_f['Описание заметки'],
                  '\nСтатус заметки:', temp_f['Статус заметки'],
                  '\nТекущая дата:', temp_f['Текущая дата'],
                  '\nДата дедлайна:', temp_f['Дата дедлайна'])
            temp_for_title = temp_for_title + 1
        elif asker == 'Нет' and titles_stat == {}:
            print('Вы не ввели новых заметок! ')
            break
        elif asker == 'Нет' or asker == '':       #Вывод введенных заметок
            print('Вы ввели следующие заметки: ')
            for i in range(len(titles_stat)):
                temp_f = titles_stat[f'Заметка {i+1}']
                print('-------------------------')
                print(f'Заметка {i+1}:',
                      '\nИмя пользователя:', temp_f['Имя пользователя'],
                      '\nЗаголовок заметки:', temp_f['Заголовок заметки'],
                      '\nОписание заметки:', temp_f['Описание заметки'],
                      '\nСтатус заметки:', temp_f['Статус заметки'],
                      '\nТекущая дата:', temp_f['Текущая дата'],
                      '\nДата дедлайна:', temp_f['Дата дедлайна'])
            break
        else:
            print('Некорректный ввод команды! ')
    return titles_stat

def append_notes_to_file():
    Note_manager = open('Note_manager.txt', 'a', encoding='utf-8')
    i = 0
    for keys in titles_stat:
        i += 1
        Note_manager.write('-------------------------\n')
        Note_manager.write(f'Заметка {i}:\n')
        temp_val = titles_stat[keys]
        for keys in temp_val:
            temp = f'{keys}: {temp_val[keys]}\n'
            Note_manager.write(temp)

    Note_manager.close()

titles_stat = create_note()
append_notes_to_file()