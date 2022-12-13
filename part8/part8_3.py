n = int(input('Введите n: '))

print(list(element * 2 for element in range(n) if element % 2))
