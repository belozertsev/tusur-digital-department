from random import randint

def print_avg():
	num1, num2, num3 = (randint(0, 100) for i in range(3))
	arythmetical_average = (num1 + num2 + num3)/3

	print(f'{num1=}, {num2=}, {num3=}' + \
		'\n' + f'{arythmetical_average=}')

print_avg()