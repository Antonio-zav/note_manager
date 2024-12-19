 # grade 1. Этап 2. Задание 2
from add_titles_loop import titles

for i in range(len(titles)):
    print(titles[i])
    num = input("Введите нужное значение для изменения статуса заметки: "
          "1 - Активна, "
          "2 - Неактивна, "
          "3 - Отложена")
    if num == 'Активна' or num == '1':
        titles[i] = titles[i] + ' Активна'
        print('Статус заметки упешно изменен на: Активна')
    elif num == 'Неактивна' or num == '2':
        titles[i] = titles[i] + ' Неактивна'
        print('Статус заметки упешно изменен на: Неактивна')
    else:
        titles[i] = titles[i] + ' Отложена'
        print('Статус заметки упешно изменен на: Отложена')
print(titles)