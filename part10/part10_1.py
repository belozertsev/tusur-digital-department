def convertToFahrenheit(temp_celsius):
	return list(map(lambda x: 1.8 * x + 32, temp_celsius))

input = [39.2, 36.5, 37.3, 37.8]
print(convertToFahrenheit(input))
