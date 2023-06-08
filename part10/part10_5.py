def foo(n):
    for x in range(n+1):
        if x == 0:
            yield -10
        elif x % 3:
            yield 45
        elif x % 5:
            yield x / 5 + 93
        else:
            yield x / 2

print(list(foo(7)))
