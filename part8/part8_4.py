def rotate90(arr):
	# внутренний цикл (по j) по столбцу (снизу вверх) формирует строку нового массива (одномерный массив)
	# внешний цикл (по i) объединяется эти строки в итоговый массив
	return [ [arr[j][i] for j in range(len(arr) - 1, -1, -1)] for i in range(len(arr[0])) ]

def decrypt(grid, kit):
	size = len(grid)

	decrypted_string = ''

	for side in range(4):
		for grid_row, kit_row in zip(grid, kit):
			for i in range(size):
				if grid_row[i] == 'X':
					decrypted_string += kit_row[i]
		grid = rotate90(grid)
	
	return decrypted_string

print('Результат для входных данных из примера:', decrypt(['X...', '..X.', 'X..X', '....'], ['itdf', 'gdce', 'aton', 'qrdi']))
