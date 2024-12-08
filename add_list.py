# grade 1. Этап 1. Задание 4

from add_input import username, content, status, created_date,issue_date

titles = []
for i in range (4):
    title = input(f'Введите заголовок заметки № {i+1}: ')
    titles.append(title)

print('Вы ввели следующие данные: ')
print('Имя пользователя: ', username)
print('Заголовок заметки: ', titles)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания заметки: ', created_date)
print('Дата истечения заметки: ', issue_date)