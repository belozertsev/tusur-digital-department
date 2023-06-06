string = input("Введите слово: ")

def isPalindrom(s):
	return s == s[-1::-1]

print(isPalindrom(string))