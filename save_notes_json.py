# grade 1. Этап 4. Задание 5

import copy,json
from datetime import date, datetime

def create_note():
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

def display_notes(titles_stat):
    i = 0
    if titles_stat != {}:
        print('Ваши заметки: ')
        for keys in titles_stat:
            i = i + 1
            print('-------------------------')
            print(f'Заметка {i}:')
            temp_val = titles_stat[keys]
            for key in temp_val:
                print(key, ':',temp_val[key])
    else:
        print('Введенных заметок нет')

def update_note(titles_stat):
    if titles_stat != {}:
        while True:
            display_notes(titles_stat)
            try:
                temp_num_title = input('Введите номер заметки которую вы хотите изменить или "Нет" если ничего менять не требуется: ')
                temp_num_title = int(int(temp_num_title) / 1)
                try:
                    temp_val = titles_stat[f'Заметка {temp_num_title}']
                    print('Выбранная заметка: ')
                    print('-------------------------')
                    print(f'Заметка {temp_num_title}',
                          '\nИмя пользователя:', temp_val['Имя пользователя'],
                          '\nЗаголовок заметки:', temp_val['Заголовок заметки'],
                          '\nОписание заметки:', temp_val['Описание заметки'],
                          '\nСтатус заметки:', temp_val['Статус заметки'],
                          '\nТекущая дата:', temp_val['Текущая дата'],
                          '\nДата дедлайна:', temp_val['Дата дедлайна'])
                    while True:
                        temp_key = input(''
                                         '\nИмя пользователя'
                                         '\nЗаголовок заметки'
                                         '\nОписание заметки'
                                         '\nСтатус заметки'
                                         '\nДата дедлайна'
                                         '\nВведите название поля которое вы хотите изменить: '
                                         ).capitalize()
                        if temp_key == 'Имя пользователя' or temp_key == 'Заголовок заметки' or temp_key == 'Описание заметки' or temp_key == 'Статус заметки' or temp_key == 'Дата дедлайна':
                            break
                        else:
                            print('Некорректный ввод значения, попробуйте снова! ')
                    temp_value_1 = titles_stat.pop(f'Заметка {temp_num_title}')
                    temp_value_2 = temp_value_1.pop(f'{temp_key}')
                    print('Значение выбранного поля:', temp_value_2)
                    if temp_key == 'Имя пользователя' or temp_key == 'Заголовок заметки' or temp_key == 'Описание заметки':
                        temp_val = input('Введите новое значение для выбранного поля: ').capitalize()
                        temp_value_1[temp_key] = temp_val
                        titles_stat[f'Заметка {temp_num_title}'] = temp_value_1
                    elif temp_key == 'Статус заметки':
                        while True:
                            temp_val = input('Введите новый статус заметки (Новая, В процессе, Выполнено): ').capitalize()
                            if temp_val == 'Новая' or temp_val == 'В процессе' or temp_val == 'Выполнено':
                                temp_value_1[temp_key] = temp_val
                                titles_stat[f'Заметка {temp_num_title}'] = temp_value_1
                                break
                            else:
                                print('Вы ввели некоректный статус заметки! ')
                    elif temp_key == 'Дата дедлайна':
                        while True:
                            temp_val = input('Введите нужную дату в формате ЧЧ.ММ.ГГГГ: ')
                            format = "%d.%m.%Y"
                            try:
                                res = bool(datetime.strptime(temp_val, format))
                                break
                            except ValueError:
                                print('Вы ввели некоректный формат даты!')
                        temp_value_1[temp_key] = temp_val
                        titles_stat[f'Заметка {temp_num_title}'] = temp_value_1
                    print(f'Значение поля "{temp_key}" успешно изменено на: {temp_val}')
                    temp_val = titles_stat[f'Заметка {temp_num_title}']
                    print(f'Заметка {temp_num_title}',
                          '\nИмя пользователя:', temp_val['Имя пользователя'],
                          '\nЗаголовок заметки:', temp_val['Заголовок заметки'],
                          '\nОписание заметки:', temp_val['Описание заметки'],
                          '\nСтатус заметки:', temp_val['Статус заметки'],
                          '\nТекущая дата:', temp_val['Текущая дата'],
                          '\nДата дедлайна:', temp_val['Дата дедлайна'])
                    while True:
                        a = input('Желаете ли снова изменить эту заметку? Да/Нет').capitalize()
                        if a == 'Да' or a == 'Нет':
                            break
                        else:
                            print('Вы ввели некоректную команду, попробуйте снова! ')
                    if a == 'Да':
                        continue
                    elif a == 'Нет':
                        print('Вы закончили замену! ')
                        break
                except KeyError:
                    print('Указанная заметка не найдена. Попробуйте снова.')
                    continue
            except ValueError:
                if temp_num_title.capitalize() == 'Нет' or temp_num_title.capitalize() == '':
                    print('Вы закончили замену! ')
                    break
                else:
                    print('Вы ввели некоректную команду, попробуйте снова! ')
        return titles_stat
    else:
        print('Нет введенных заметок')

def search_notes(titles_stat):
    temp_dict = copy.deepcopy(titles_stat)
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
        temp_keyword = input('Введите ключевое слово: ').lower()
        for i in range(len(temp_dict)):
            t = str(i + 1)
            temp_item = temp_dict.pop(f'Заметка {t}')
            temp_us = temp_item.pop('Имя пользователя')
            temp_tit = temp_item.pop('Заголовок заметки')
            temp_con = temp_item.pop('Описание заметки')
            if temp_keyword in temp_us.lower() or temp_keyword in temp_tit.lower() or temp_keyword in temp_con.lower():
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
        temp_keyword_1 = input('Введите ключевое слово: ').lower()
        while True:
            temp_keyword_2 = input('Введите статус заметки (Новая, В процессе, Выполнено): ').capitalize()
            if temp_keyword_2 == 'Новая' or temp_keyword_2 == 'В процессе' or temp_keyword_2 == 'Выполнено':
                break
            else:
                print('Вы ввели некоректный статус заметки! ')
        for i in range(len(temp_dict)):
            t = str(i + 1)
            temp_item = temp_dict.pop(f'Заметка {t}')
            temp_stat = str(temp_item.pop('Статус заметки')).lower()
            if temp_keyword_2.lower() in temp_stat:
                temp_dict_1 = {}
                temp_dict_1[f'Заметка {t}'] = copy.deepcopy(titles_stat[f'Заметка {t}'])
                temp_item = temp_dict_1.pop(f'Заметка {t}')
                temp_us = temp_item.pop('Имя пользователя')
                temp_tit = temp_item.pop('Заголовок заметки')
                temp_con = temp_item.pop('Описание заметки')
                if temp_keyword_1 in temp_us.lower() or temp_keyword_1 in temp_tit or temp_keyword_1 in temp_con.lower():
                    print('-------------')
                    temp_val = titles_stat[f'Заметка {t}']
                    print(f'Заметка {t}',
                          '\nИмя пользователя', temp_val['Имя пользователя'],
                          '\nЗаголовок заметки', temp_val['Заголовок заметки'],
                          '\nОписание заметки', temp_val['Описание заметки'],
                          '\nСтатус заметки', temp_val['Статус заметки'],
                          '\nТекущая дата', temp_val['Текущая дата'],
                          '\nДата дедлайна', temp_val['Дата дедлайна'])
                else:
                    print('Заметок не найдено')
            else:
                print('Заметок не найдено')
    elif temp_num_of_search == 4:
        print('Поиск был отменен. ')

def delete_note(titles_stat):
    while True:
        temp = input('Введите номер заметки которую следует удалить: ')
        try:
            temp = int(temp)
            try:
                a = titles_stat.pop(f'Заметка {temp}')
                print(f'Вы удалили следующую заметку:',
                      '\nИмя пользователя:', a['Имя пользователя'],
                      '\nЗаголовок заметки:', a['Заголовок заметки'],
                      '\nОписание заметки:', a['Описание заметки'],
                      '\nСтатус заметки:', a['Статус заметки'],
                      '\nТекущая дата:', a['Текущая дата'],
                      '\nДата дедлайна:', a['Дата дедлайна'])
                break
            except ValueError:
                print('Заметка не найдена')
                while True:
                    a = input('Хотите ли вы продолжить удаление? Да/Нет')
                    if a == 'Да' or a == 'Нет':
                        break
                    else:
                        print('Вы ввели некоректную команду, попробуйте снова!')
                if a == 'Да':
                    continue
                elif a == 'Нет':
                    break


        except ValueError:
            print('Вы ввели некоректную команду, попробуйте снова!')
    return titles_stat

def menu():
    print('Здравствуйте пользователь!')
    while True:
        print('----------------------')
        print('Меню:'
              '\n1 - Создание заметок'
              '\n2 - Показать все заметки'
              '\n3 - Обновить заметку'
              '\n4 - Удалить заметку'
              '\n5 - Найти заметки'
              '\n6 - Выйти из программы')
        ask_num = input('Выберите нужное действие из меню: ')
        try:
            ask_num = int(ask_num)
            if ask_num == 1:
                create_note()
            elif ask_num == 2:
                display_notes(titles_stat)
            elif ask_num == 3:
                update_note(titles_stat)
            elif ask_num == 4:
                display_notes(titles_stat)
                delete_note(titles_stat)
            elif ask_num == 5:
                search_notes(titles_stat)
            elif ask_num == 6:
                print('Досвидания!!!')
                break
            else:
                print('Вы ввели недопустимую команду')
        except ValueError:
            print('Вы ввели недопустимую команду')

def save_notes_json(note):
    try:
        with open('Note_manager.json', 'w', encoding='utf-8') as Note_manager:
            json.dump(note, Note_manager, ensure_ascii=False, indent=4)
    except:
        print('Проблема с сохранением в файл. Пустой файл будет создан')
        with open('Note_manager.json', 'w', encoding='utf-8') as Note_manager:
            pass

titles_stat = {}
note = menu()
save_notes_json(note)
