def draw_carpet(height = 1):
	width = 3 * height
	# Top part
	pattern = '.|.'
	for i in range(0, height//2):
		amount = (2 * i + 1)
		print((pattern * amount).center(width, '-'))

	# Middle part
	print('WELCOME'.center(width, '-'))

	# Bottom part
	for i in range(height//2, 0, -1):
		amount = (2 * i - 1)
		print((pattern * amount).center(width, '-'))

draw_carpet(5)