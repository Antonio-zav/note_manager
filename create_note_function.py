# grade 1. Этап 3. Задание 1

from datetime import date, datetime

titles_stat = {}

#Определяю функцию
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
            print('Введенная заметка: ',temp_f)
            temp_for_title = temp_for_title + 1
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

create_note() #Вызов функции