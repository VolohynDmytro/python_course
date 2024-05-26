from inspect import isgenerator


def action(x):
    return x ** 2


def some_gen(begin, end, func):
    i = 0
    while i <= end - 1:
        yield begin
        begin = func(begin)
        i += 1


gen = some_gen(2, 4, action)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
