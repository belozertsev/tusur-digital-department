tpl = tuple(map(int, input('Введите элементы кортежа через пробел: ').split()))

print('Введенный кортеж:', tpl)
print('Отсортированный по абсолютным значениям:', sorted(tpl, key=abs))
