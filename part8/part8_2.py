str_input = input('Введите x, y, z, n через пробел: ').split()
array = [int(number) for number in str_input]

def myGenerator(arr, n):
	for i in range(3):
		for j in range(3):
			for k in range(3):
				if arr[i] + arr[j] + arr[k] != n:
					yield (arr[i], arr[j], arr[k])

variants = {variant for variant in myGenerator(array[:3:], array[3])}

print(variants)