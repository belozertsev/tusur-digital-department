str = input('Введите текст: ')

result = "Результат: "
for letter in str:
    if letter.isupper():
        result += letter
print(result)
