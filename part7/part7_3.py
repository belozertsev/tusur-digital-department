import random

rates = {
    'Sberbank': 55.8,
    'VTB24': 53.91,
    'Tinkoff': random.uniform(50, 60)
}

rates_swapped = dict((value, key) for key, value in rates.items())
best_rate = min(rates_swapped.keys())

print(f'Список курсов:\n{rates}')
print(f'Лучший курс ({best_rate:,.2f}) - в банке {rates_swapped[best_rate]}')
