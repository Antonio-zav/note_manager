 # grade 1. Этап 2. Задание 2

from add_titles_loop import titles

titles_stat = {}
for i in range(len(titles)):
    print('Заметка: ', titles[i])
    num = input("Введите нужное значение для изменения статуса заметки: "
          "1 - Активна, "
          "2 - Неактивна, "
          "3 - Отложена ")
    if num.capitalize() == 'Активна' or num == '1':
        titles_stat.update({titles[i]: ' Активна'})
        print('Статус заметки упешно изменен на: Активна')
    elif num.capitalize() == 'Неактивна' or num == '2':
        titles_stat.update({titles[i]: ' Неактивна'})
        print('Статус заметки упешно изменен на: Неактивна')
    else:
        titles_stat.update({titles[i]: ' Отложена'})
        print('Статус заметки упешно изменен на: Отложена')
print(titles_stat)