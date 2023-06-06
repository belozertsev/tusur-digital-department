n = int(input("Введите число N: "))

def numberToReversedList(number):
	return [int(char) for char in str(number)[-1::-1]]

print(numberToReversedList(n))