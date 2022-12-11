tokens = input('Введите текст: ').strip().split()

counter = 0

for token in tokens:
	if token.isalpha():
		counter += 1
		if counter == 3: break
	else:
		counter = 0

print(counter == 3)
