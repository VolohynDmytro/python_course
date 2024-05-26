from inspect import isgenerator


def generate_cube_numbers(end):
    start_point = 2
    cont = 0
    while cont <= end:
        yield start_point ** 3
        start_point += 1
        cont = start_point ** 3


gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print("OKAY")
