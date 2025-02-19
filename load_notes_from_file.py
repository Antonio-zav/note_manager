# grade 1. Этап 4. Задание 2

def load_notes_from_file():
    try:
         with open('Note_manager.txt', 'r', encoding='utf-8') as Note_manager:
            temp_str = Note_manager.read()
            if temp_str == 'Ваши заметки:\n' or temp_str == '':
                print('Список заметок пуст!')
            else:
                temp_str = temp_str.replace('\n','|')
                temp_str = temp_str.replace('Ваши заметки:|','')
                temp_str = temp_str.replace('-------------------------|','')
                temp_str = temp_str.replace('Имя пользователя: ', '')
                temp_str = temp_str.replace('Заголовок заметки: ', '')
                temp_str = temp_str.replace('Описание заметки: ', '')
                temp_str = temp_str.replace('Статус заметки: ', '')
                temp_str = temp_str.replace('Текущая дата: ', '')
                temp_str = temp_str.replace('Дата дедлайна: ', '')
                for i in range(len(temp_str)):
                    temp_str = temp_str.replace(f'Заметка {i}:|', '')
                temp_str = temp_str[:-1]
                temp_str = temp_str.split('|')
                temp_stat = {}
                note = []
                while temp_str:
                    temp_stat['username'] = temp_str.pop(0)
                    temp_stat['title'] = temp_str.pop(0)
                    temp_stat['content'] = temp_str.pop(0)
                    temp_stat['status'] = temp_str.pop(0)
                    temp_stat['current_date'] = temp_str.pop(0)
                    temp_stat['issue_date'] = temp_str.pop(0)
                    note.append(temp_stat)
                    temp_stat = {}
                    print(note)


    except FileNotFoundError:
        print('Файл не найден')
        with open('Note_manager.txt', 'w', encoding='utf-8') as Note_manager:
            print('Новый файл был создан')
    except IndexError:
        print('Данные введенны не в нужном формате. Проверьте содержимое')
    except PermissionError:
        print('Ошибка доступа')

load_notes_from_file()