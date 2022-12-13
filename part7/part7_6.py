def check(data):
	win_states = ['XXX', 'OOO']
	
	# checking for rows
	for row in data:
		if row in win_states:
			return row[0]

	# checking for columns
	for i in range(0,2):
		col = ''.join([row[i] for row in data])
		if col in win_states:
			return col[0]

	# checking for diagonals
	straight_diagonal = str([data[0][0], data[1][1], data[2][2]])
	counter_diagonal = str([data[0][2], data[1][1], data[2][0]])
	if straight_diagonal in win_states or counter_diagonal in win_states:
		return data[1][1]

	return 'D'

data = input('Введите три строки, разделяя их пробелами: ').upper().split()
print('Победитель -', check(data))