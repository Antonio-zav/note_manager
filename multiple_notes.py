# grade 1. Этап 2. Задание 4

#Импорт заголовков
from datetime import date
from add_titles_loop import titles, username

current_date = str(date.today())
current_date_d= int(current_date[8:])
current_date_m = int(current_date[5:7])
#Запрос активности заметки или её удаление

titles_stat = {}
for i in range(len(titles)):
    print('Заметка: ', titles[i])
    num = input("Введите нужное значение для изменения статуса заметки: "
          "1 - Активна, "
          "2 - Неактивна, "
          "3 - Отложена "
          "4 - Удалить заметку ")
    if num.capitalize() == 'Активна' or num == '1':
        print('Статус заметки упешно изменен на: Активна')
        while True:
            temp_date = input('Введите необходимую дату в формате ЧЧ.ММ.ГГГГ: ')
            temp_date_d = int(temp_date[0:2])
            temp_date_m = int(temp_date[3:5])
            if temp_date_d > current_date_d and temp_date_m <= current_date_m:
                titles_stat.update({titles[i]: (' Активна', temp_date)})
                break
            else:
                print('Вы ввели уже прошедшую дату!! Попробуйте снова. ')

    elif num.capitalize() == 'Неактивна' or num == '2':
        titles_stat.update({titles[i]: ' Неактивна'})
        print('Статус заметки упешно изменен на: Неактивна')
    elif num.capitalize() == 'Удалить' or num == '4':
        var = titles.pop(i)
        print("Вы удалили заметку: ", var)
    else:
        titles_stat.update({titles[i]: ' Отложена'})
        print('Статус заметки упешно изменен на: Отложена')
print('Ваша Фамилия: ', username)
print('Текущее время: ', current_date)
print('Все ваши заголовки: ', titles_stat)