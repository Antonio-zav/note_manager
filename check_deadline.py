# # grade 1. Этап 2. Задание 3

from datetime import date, datetime

current_date = str(date.today())
while True:
    issue_date = input('Введите нужную дату в формате ЧЧ.ММ.ГГГГ: ')
    format = "%d.%m.%Y"
    try:
        res = bool(datetime.strptime(issue_date, format))
        break
    except ValueError:
        print ('Вы ввели некоректный формат даты!')

current_date_d= int(current_date[8:])
current_date_m = int(current_date[5:7])
current_date_y = int(current_date[0:4])

issue_date_d = int(issue_date[0:2])
issue_date_m = int(issue_date[3:5])
issue_date_y = int(issue_date[6:])

if current_date_d < issue_date_d and current_date_m <= issue_date_m and current_date_y <= issue_date_y:
    print(f'До окончаию заметки ещё осталось {issue_date_d - current_date_d} дней! ')
elif current_date_d == issue_date_d and current_date_m == issue_date_m:
    print('Срок заметки окончится сегодня!!!')
else:
    print('Срок вашей заметки истек', current_date_d - issue_date_d, 'дней назад')
print(issue_date, '- Дата создания заметки')
print(current_date, '- Текущая дата')


