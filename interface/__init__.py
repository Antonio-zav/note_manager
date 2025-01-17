# Интерфейсные функции для работы с заметками

from utils import *
from data import *

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

def menu(titles_stat):
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
                create_note(titles_stat)
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
    return titles_stat