def find_unique_value(some_list: list) -> int:
    for elem in some_list:
        res = some_list.count(elem)
        if res == 1:
            return elem
        else:
            continue


assert find_unique_value([1, 2, 1, 1]) == 2
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5
print("ОК")
