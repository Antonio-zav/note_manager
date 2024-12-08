# grade 1. Этап 1. Задание 2

from datetime import datetime
from greetings import issue_date

issue_date = input('Введите дату в формате ЧЧ.ММ.ГГГГ: ')
print(issue_date)
issue_date_d = int(issue_date[0:2])
issue_date_m = int(issue_date[3:5])
issue_date_y = int(issue_date[6:])
print(issue_date_d, issue_date_m)