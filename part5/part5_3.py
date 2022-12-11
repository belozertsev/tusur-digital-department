N = int(input('Введите число: '))

while N < 1 or N > 9:
	N = int(input('Введённое число некорректно, введите новое от 1 до 9: '))

result = ""
for i in range(1, N + 1):
	result += str(i)
print(result)
