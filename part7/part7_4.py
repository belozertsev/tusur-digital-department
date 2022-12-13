initial_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5
}

swapped_dict = dict((key, value) for value, key in initial_dict.items())

print(f'Исходный словарь: {initial_dict}')
print(f'Получившийся словарь: {swapped_dict}')
