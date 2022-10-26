from random import randint


def print_things():
	num1, num2 = (randint(1, 100) for i in range(2))
	print(f'{num1=}, {num2=}')
	print(num1 // num2, num1 % num2)

print_things()