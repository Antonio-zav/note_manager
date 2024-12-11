# импортирую нужные данные из других файлов
from add_input import username, content, status
from add_list import titles
from date_changer import temp_created_date, temp_issue_date

# Создаю список
note = {}
note['username'] = username
note['content'] = content
note['status'] = status
note['created_date'] = temp_created_date
note['issue_date'] = temp_issue_date
note['titles'] = titles

# Выводим собранные данные

print('\nСобранная информация о заметке: ')
for key, value in note.items():
    print(f'{key.capitalize()}: {value}')
