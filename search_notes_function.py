# grade 1. Этап 3. Задание 4
from datetime import date, datetime
import copy

def create_note():
    temp_for_title = 1
    titles_stat = {}
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
            print('Введенная заметка: ',temp_f)
            temp_for_title = temp_for_title + 1
        elif asker == 'Нет' and titles_stat == {}:
            print('Вы не ввели новых заметок! ')
            break
        elif asker == 'Нет' or asker == '':       #Вывод введенных заметок
            print('Вы ввели следующие заметки: ')
            i = 1
            for keys in titles_stat:
                print('')
                print(f'Заметка {i} ', titles_stat[keys])
                i = i + 1
            break
        else:
            print('Некорректный ввод команды! ')
    return titles_stat

def search_notes(title_stat, keyword = None, status = None):
    while True:
        temp_num_of_search = input('Введите номер нужного формата поиска'
                                   '\n1 - Поиск по ключевому слову'
                                   '\n2 - Поиск по статусу заметки'
                                   '\n3 - Поиск по ключевому слову и статусу'
                                   '\n4 - Отмена поиска'
                                   '\n')
        try:
            temp_num_of_search = int(temp_num_of_search)
            if temp_num_of_search == 1 or temp_num_of_search == 2 or temp_num_of_search == 3 or temp_num_of_search == 4:
                break
            else:
                print('Неправильный формат ввода, попробуйте снова!')
        except ValueError:
            print('Неправильный формат ввода, попробуйте снова!')
    if temp_num_of_search == 1:
        temp_keyword = input('Введите ключевое слово: ').capitalize()
        for i in range(len(temp_dict)):
            t = str(i + 1)
            temp_item = temp_dict.pop(f'Заметка {t}')
            temp_us = temp_item.pop('Имя пользователя')
            temp_tit = temp_item.pop('Заголовок заметки')
            temp_con = temp_item.pop('Описание заметки')
            if temp_keyword in temp_us or temp_keyword in temp_tit or temp_keyword in temp_con:
                print('-------------')
                temp_val = titles_stat[f'Заметка {t}']
                print(f'Заметка {t}',
                      '\nИмя пользователя', temp_val['Имя пользователя'],
                      '\nЗаголовок заметки', temp_val['Заголовок заметки'],
                      '\nОписание заметки', temp_val['Описание заметки'],
                      '\nСтатус заметки', temp_val['Статус заметки'],
                      '\nТекущая дата', temp_val['Текущая дата'],
                      '\nДата дедлайна', temp_val['Дата дедлайна'])
    elif temp_num_of_search == 2:
        while True:
            temp_keyword = input('Введите статус заметки (Новая, В процессе, Выполнено): ').capitalize()
            if temp_keyword == 'Новая' or temp_keyword == 'В процессе' or temp_keyword == 'Выполнено':
                break
            else:
                print('Вы ввели некоректный статус заметки! ')
        for i in range(len(temp_dict)):
            t = str(i + 1)
            temp_item = temp_dict.pop(f'Заметка {t}')
            temp_stat = temp_item.pop('Статус заметки')
            if temp_keyword in temp_stat:
                print('-------------')
                temp_val = titles_stat[f'Заметка {t}']
                print(f'Заметка {t}',
                      '\nИмя пользователя', temp_val['Имя пользователя'],
                      '\nЗаголовок заметки', temp_val['Заголовок заметки'],
                      '\nОписание заметки', temp_val['Описание заметки'],
                      '\nСтатус заметки', temp_val['Статус заметки'],
                      '\nТекущая дата', temp_val['Текущая дата'],
                      '\nДата дедлайна', temp_val['Дата дедлайна'])
    elif temp_num_of_search == 3:
        temp_keyword_1 = input('Введите ключевое слово: ').capitalize()
        while True:
            temp_keyword_2 = input('Введите статус заметки (Новая, В процессе, Выполнено): ').capitalize()
            if temp_keyword_2 == 'Новая' or temp_keyword_2 == 'В процессе' or temp_keyword_2 == 'Выполнено':
                break
            else:
                print('Вы ввели некоректный статус заметки! ')
        for i in range(len(temp_dict)):
            t = str(i + 1)
            temp_item = temp_dict.pop(f'Заметка {t}')
            temp_stat = temp_item.pop('Статус заметки')
            if temp_keyword_2 in temp_stat:
                temp_dict_1 = {}
                temp_dict_1[f'Заметка {t}'] = copy.deepcopy(titles_stat[f'Заметка {t}'])
                temp_item = temp_dict_1.pop(f'Заметка {t}')
                temp_us = temp_item.pop('Имя пользователя')
                temp_tit = temp_item.pop('Заголовок заметки')
                temp_con = temp_item.pop('Описание заметки')
                if temp_keyword_1 in temp_us or temp_keyword_1 in temp_tit or temp_keyword_1 in temp_con:
                    print('-------------')
                    temp_val = titles_stat[f'Заметка {t}']
                    print(f'Заметка {t}',
                          '\nИмя пользователя', temp_val['Имя пользователя'],
                          '\nЗаголовок заметки', temp_val['Заголовок заметки'],
                          '\nОписание заметки', temp_val['Описание заметки'],
                          '\nСтатус заметки', temp_val['Статус заметки'],
                          '\nТекущая дата', temp_val['Текущая дата'],
                          '\nДата дедлайна', temp_val['Дата дедлайна'])
    elif temp_num_of_search == 4:
        print('Поиск был отменен. ')

titles_stat = create_note()
temp_dict = copy.deepcopy(titles_stat)
search_notes(titles_stat)
