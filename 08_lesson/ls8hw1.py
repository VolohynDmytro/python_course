def add_one(some_list: list) -> list:
    final_list = []
    number = int(''.join(map(str, some_list))) + 1
    str_to_new_list = str(number)
    for elem in str_to_new_list:
        final_list.append(int(elem))
    return final_list


if __name__ == "__main__":
    assert add_one([1, 2, 3, 7]) == [1, 2, 3, 8]
    assert add_one([9, 9, 9]) == [1, 0, 0, 0]
    assert add_one([0]) == [1]
    assert add_one([9]) == [1, 0]
    print("ОК")
