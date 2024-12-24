# grade 1. Этап 2. Задание 1
titles = []
i = 0
title = ''

#Запрос никнейма

username = input('Введите вашу Фанимилию: ')

while title.capitalize() != 'Нет':
    n = input('Хотите добавить ещё одну заметку Да/Нет? ')
    if n.capitalize() == 'Да':
        i = i + 1
        title = input(f'Введите заголовок заметки № {i}: ')
        titles.append(title)
    elif n.capitalize() == 'Нет':
        break
    else: continue

print('Ваши заголовки: ', titles)
