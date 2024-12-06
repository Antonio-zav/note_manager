# grade 1. Этап 1. Задание 2

from datetime import datetime
from greetings import issue_date

issue_date = input('Введите дату в формате ЧЧ-ММ-ГГГГ: ')
print(issue_date)
datetime.strptime(issue_date, '%d.%m.%Y')
print(issue_date, type(issue_date))