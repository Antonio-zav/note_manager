# grade 1. Этап 2. Задание 4
from multiple_notes import titles_stat, current_date
from add_titles_loop import username

while True:
    delete_ask = input('Хотите ли вы удалить некоторые заметки Да/Нет? ')
    if delete_ask.capitalize() == 'Да':
        print(titles_stat)
        delete_ask = input('Введите название заметки которую хотите удалить: ')
        for key in titles_stat:
            if delete_ask == key:
                var = titles_stat.pop(key)
                print(f'Вы удалили заметку: {var}')
                break
    elif delete_ask.capitalize() == 'Нет':
        break
    else:
        print('Вы ввели неправильную команду')
        continue
    break

print('Ваша Фамилия: ', username)
print('Текущее время: ', current_date)
print('Все ваши заголовки: ', titles_stat)
