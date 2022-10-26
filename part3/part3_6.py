def multiply_digits(value = 1):
	m_result = 1 # multiplication result
	while value:
		current_digit = value % 10
		value //= 10
		if not current_digit: continue
		m_result *= current_digit
	print(m_result)

multiply_digits(123405)