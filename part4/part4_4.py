def reverse_number(number):
	sign = -1 if number < 0 else 1
	number = abs(number)
	reversed_number = 0
	while number: 
		current_digit = number % 10
		number //= 10
		reversed_number = reversed_number * 10 + current_digit
	return reversed_number * sign

# print(reverse_number(1234_0_9876))
print(reverse_number(-3205))