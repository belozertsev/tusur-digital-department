import re

text = input('Введите текст: ').lower()

# []+ - один или несколько символов из группы []
lst = re.split('[ ,.!?;:() \[\] "`\'-]+', text)

words = list(filter(None, lst))
letters = ''.join(words)

popular_words = {}
popular_letters = {}

for word in set(words):
	popular_words[word] = words.count(word)

for letter in set(letters):
	popular_letters[letter] = letters.count(letter)

print('Словарь популярных слов:', popular_words)
print('Словарь популярных букв:', popular_letters)