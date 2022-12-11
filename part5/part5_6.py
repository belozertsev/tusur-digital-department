raw = input('Введите слова по одному через запятую: ')
words = raw.split(', ')

counter = 0
for word in words:
	words[counter] = word.replace('right','left')
	counter += 1

result = ','.join(words)

print('Результат: ', result)
