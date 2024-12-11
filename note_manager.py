# grade 1. Этап 1. Задание 2

# Импортирую нужные данные
from add_input import issue_date, created_date

# Разделяю и преобразую дни, месяцы и года в int
created_date_d = int(created_date[0:2])
created_date_m = int(created_date[3:5])
created_date_y = int(created_date[6:])
print('Сегодняшняя дата:', created_date_d, '.', created_date_m)    #Вывод текущей даты без вывода года

issue_date_d = int(issue_date[0:2])
issue_date_m = int(issue_date[3:5])
issue_date_y = int(issue_date[6:])
print('Нужная дата:', issue_date_d, '.', issue_date_m)             #Вывод нужной даты без вывода года