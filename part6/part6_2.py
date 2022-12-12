lst = list(map(float, input('Введите элементы списка через пробел: ').split()))

print('Введенный список:', lst)
print('Разница между самым большим и самым малым числами:', max(lst) - min(lst) if lst else 0)
