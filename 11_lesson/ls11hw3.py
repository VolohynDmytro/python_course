def is_even(number):
    end = str(number)[-1]
    if end == '0' or end == '2' or end == '4' or end == '6' or end == '8':
        return True
    else:
        return False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OKAY')
