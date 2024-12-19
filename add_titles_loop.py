# grade 1. Этап 2. Задание 1
titles = []
i = 0
title = ''
while title != 'стоп':
    i = i + 1
    titles.append(title)
    title = input(f'Введите заголовок заметки № {i}: ')

titles.remove('')
print('Ваши заголовки: ', titles)
