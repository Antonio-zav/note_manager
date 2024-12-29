# grade 1. Этап 3. Задание 3

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
                if status == 'Новая' or status == 'В процессе' or status == 'Новая':
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

def update_note(titles_stat):
    if titles_stat != {}:
        while True:
            temp_num_title = input('Введите номер заметки которую вы хотите изменить или "Нет" если ничего менять не требуется: ')
            try:
                temp_num_title = int(int(temp_num_title) / 1)
                print('Выбранная заметка: ', titles_stat[f'Заметка {temp_num_title}'])
                while True:
                    temp_key = input('Введите название поля которое вы хотите изменить: '
                                     '\nИмя пользователя'
                                     '\nЗаголовок заметки'
                                     '\nОписание заметки'
                                     '\nСтатус заметки'
                                     '\nДата дедлайна'
                                     '\n'
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
                        status = input('Введите новый статус заметки (Новая, В процессе, Выполнено): ').capitalize()
                        if status == 'Новая' or status == 'В процессе' or status == 'Выполнено':
                            temp_value_1[temp_key] = status
                            titles_stat[f'Заметка {temp_num_title}'] = temp_value_1
                            break
                        else:
                            print('Вы ввели некоректный статус заметки! ')
                elif temp_key == 'Дата дедлайна':
                    while True:
                        issue_date = input('Введите нужную дату в формате ЧЧ.ММ.ГГГГ: ')
                        format = "%d.%m.%Y"
                        try:
                            res = bool(datetime.strptime(issue_date, format))
                            break
                        except ValueError:
                            print('Вы ввели некоректный формат даты!')
                    temp_value_1[temp_key] = issue_date
                    titles_stat[f'Заметка {temp_num_title}'] = temp_value_1
                print('Значение поля успешно изменено!')
            except ValueError:
                if temp_num_title.capitalize() == 'Нет' or temp_num_title.capitalize() == '':
                    print('Вы закончили замену! ')
                    break
                else:
                    print('Вы ввели некоректную команду, попробуйте снова! ')
        k = 1
        for keys in titles_stat:
            print('')
            print(f'Заметка {k} ', titles_stat[keys])
            k = k + 1
        return titles_stat

def display_notes(titles_stat):
    i = 0
    for keys in titles_stat:
        i = i + 1
        print('-------------------------')
        print(f'Заметка {i}:')
        temp_val = titles_stat[keys]
        for keys in temp_val:
            print(keys, ':',temp_val[keys])

titles_stat = {}

titles_stat = create_note()
titles_stat = update_note(titles_stat)
display_notes(titles_stat)


