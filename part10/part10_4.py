def powForEach(x, y):
    return list(value**power for value, power in zip(x, y))

x = [2, 3, 4]
y = [10, 11, 12]

print(powForEach(x, y))
