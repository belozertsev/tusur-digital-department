str_input = input('Введите массив целых числе (разделяя пробелами): ').split()

integers = [int(number) for number in str_input]

nonUnique = [number for number in integers if integers.count(number) != 1]

print(nonUnique)
