dates = ['2017-03-01', '2017-03-02']
rates = [55.7, 55.2]

dates_and_rates = dict((date, rate) for date, rate in zip(dates, rates))

print(f'Список дат: {dates}')
print(f'Список курсов: {rates}')
print(f'Получившийся словарь: {dates_and_rates}')
