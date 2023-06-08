from functools import reduce

def maximum_below(level, lst):
    '''
        В этой функции находится максимальное значение площади
        для заданного уровня level.

		На тестовом списке [2, 1, 4, 5, 1, 3, 3]
		для level=2 в конце состояние буфера будет [2, 4, 4]
		для level=4 в конце состояние буфера будет [8, 6]
		для level=5 в конце состояние буфера будет [5]
    '''
    
    lst.append(0)
    buffer = []
    flag = 0
    counter = 0
    for val in lst:
        if val >= level:
            counter += 1
            flag = 1
        if flag and val < level:
            flag = 0
            buffer.append(counter * level)
            counter = 0
            
    return max(buffer)

def maximum_overall(lst):
    return max(maximum_below(lvl, lst) for lvl in range(1, max(lst) + 1))

inp = [2, 1, 4, 5, 1, 3, 3]
print(maximum_overall(inp))
