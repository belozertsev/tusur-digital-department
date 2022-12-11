number = int(input('Enter a number: '))

result = ''

if number % 3 == 0:
	result += 'Fizz '

if number % 5 == 0:
	result += 'Buzz'

if result:
	print(result.rstrip())
else:
	print(number)
	