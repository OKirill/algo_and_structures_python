"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

company = namedtuple('company', ['name', 'quarter_income', 'income'])

count_quarter = 4
company_set = set()
total_income = 0

n = int(input('Введите кол-во предприятий: '))

for i in range(1, n + 1):
    income = 0
    incomes = []
    name = input(f'Введите наименования предприятий {i}: ')

    for j in range(count_quarter):
        incomes.append(int(input(f'Введите прибыль за {j + 1}-й квартал: ')))
        income += incomes[j]

    f = company(name=name, quarter_income=tuple(incomes), income=income)
    company_set.add(f)
    total_income += income

middle_income = total_income / n
print('Средняя годовая прибыль всех предприятий: ', middle_income)

print(f'\nПредприятия у которых прибыль выше среднего:')
for f in company_set:
    if f.income > middle_income:
        print(f'Прибыль фирмы {f.name} - {f.income}')

print(f'\nПредприятия у которых прибыль ниже среднего:')
for f in company_set:
    if f.income < middle_income:
        print(f'Прибыль фирмы {f.name} - {f.income}')
