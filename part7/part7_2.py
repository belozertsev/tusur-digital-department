number = int(input('Введите число от 1 до 3999: '))

while number not in range(1, 4000):
    number = int(input('Число не входит в диапазон! Введите новое: '))

ArabicToRoman = [
	(1000, 'M'),
	(900, 'CM'),
	(500, 'D'),
	(400, 'CD'),
	(100, 'C'),
	(90, 'XC'),
	(50, 'L'),
	(40, 'XL'),
	(10, 'X'),
	(9, 'IX'),
	(5, 'V'),
	(4, 'IV'),
	(1, 'I')
]

result = ''
for arabic, roman in ArabicToRoman:
	result += number // arabic * roman
	number %= arabic

print('Число в римской системе:', result)
