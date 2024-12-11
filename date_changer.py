# grade 1. Этап 1. Задание 2

# Импортирую нужные данные
from add_input import issue_date, created_date

# Разделяю дни, месяцы и года
created_date_d = created_date[0:2]
created_date_m = created_date[3:5]
created_date_y = created_date[6:]
temp_created_date = created_date_d + '.' + created_date_m
# print('Сегодняшняя дата:', temp_created_date)    #Вывод текущей даты без вывода года

issue_date_d = issue_date[0:2]
issue_date_m = issue_date[3:5]
issue_date_y = issue_date[6:]
temp_issue_date = issue_date_d + '.' + issue_date_m
# print('Нужная дата:', temp_issue_date)             #Вывод нужной даты без вывода года