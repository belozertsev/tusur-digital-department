lst = list(map(int, input('Введите элементы списка через пробел: ').split()))

print('Введенный список:', lst)

lst = sorted(lst)
len_lst = len(lst)

mediana = lst[len_lst // 2] if len_lst % 2 else (lst[len_lst // 2] + lst[len_lst // 2 - 1]) / 2

print('Медиана списка:', mediana)
