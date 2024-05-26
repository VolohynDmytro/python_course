from inspect import isgenerator


def prime_generator(end):
    div_count = 0
    for i in range(2, end + 1):
        for j in range(2, i):
            if i % j == 0:
                div_count = + 1
        if div_count == 0:
            yield i
        else:
            div_count = 0


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
