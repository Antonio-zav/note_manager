# импортирую нужные данные из других файлов
from add_input import username, content, status, created_date, issue_date
from add_list import titles

# Создаю список
note = {}
note['username'] = username
note['content'] = content
note['status'] = status
note['created_date'] = created_date
note['issue_date'] = issue_date
note['titles'] = titles

# Выводим собранные данные

print('\nСобранная информация о заметке: ')
for key, value in note.items():
    print(f'{key.capitalize()}: {value}')
