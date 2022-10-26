def round_2f(value):
	return round(value, 2)

def round_to_an_integer(value):
	return round(value)

def round_to_11_digigts(value):
	return str(value).zfill(11)

given_number = 152.12514
print(f'{given_number=}')
print(round_2f(given_number), round_to_an_integer(given_number), round_to_11_digigts(given_number))