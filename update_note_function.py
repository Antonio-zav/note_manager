# grade 1. Этап 3. Задание 2

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

titles_stat = {}
titles_stat = create_note()
update_note(titles_stat)