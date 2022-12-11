x = int(input('Введите число: '))

if x % 2 != 0:
	print("Плохо")
elif x >= 2 and x <= 5:
	print("Неплохо")
elif x >= 6 and x <= 20:
	print("Так себе")
elif x > 20:
	print("Отлично")
else:
	print("Число чётное, но отрицательное")
	