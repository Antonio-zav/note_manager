# grade 1. Этап 3. Задание 1

from datetime import date, datetime

titles_stat = {}

#Определяю функцию
def create_note():
    temp_for_title = 1
    while True:
        asker = input('Вы хотите добавить новую заметку? Да/Нет ')
        if asker.capitalize() == 'Да':                  # Создание заметки
            username = input('Введите имя пользователя: ')
            title = input('Введите заголовок заметки: ')
            content = input('Введите описание заметки: ')
            current_date = str(date.today())
            while True:
                status = input('Введите статус заметки (Новая, В процессе, Выполнено): ')
                if status.capitalize() == 'Новая' or status.capitalize() == 'В процессе' or status.capitalize() == 'Новая':
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
            titles_stat[f'Заметка {temp_for_title} '] = {
                'Имя пользователя: ':  username ,
                'Заголов заметки: ': title,
                'Описание заметки: ': content,
                'Статус заметки: ': status,
                'Текущая дата: ': current_date,
                'Дата дедлайна: ': issue_date
            }
            temp_f = titles_stat[f'Заметка {temp_for_title} ']
            print('Введенная заметка: ',temp_f)
            temp_for_title = temp_for_title + 1
        elif asker.capitalize() == 'Нет' or asker.capitalize() == '':       #Вывод введенных заметок
            print('Вы ввели следующие заметки: ')
            i = 1
            for key in titles_stat:
                print(f'Заметка {i}')
                print(titles_stat[key])
                i = i + 1
            break
        else:
            print('Некорректный ввод команды! ')

create_note() #Вызов функции