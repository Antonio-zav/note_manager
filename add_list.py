# grade 1. Этап 1. Задание 4

# импортирую нужные данные из других файлов
from add_input import username, content, status, created_date,issue_date

# Создаю список
titles = []
for i in range (4):
    title = input(f'Введите заголовок заметки № {i+1}: ')
    titles.append(title)

# Вывод данных для проверки
# print('Заголовок заметки: ', titles)
