def common_elements():
    list_one = []
    list_two = []
    for i in range(100):
        if i % 3 == 0:
            list_one.append(i)

    for i in range(100):
        if i % 5 == 0:
            list_two.append(i)
    final_list = list(set(list_one) & set(list_two))
    return final_list


assert common_elements() == [0, 75, 45, 15, 90, 60, 30]
print('all good')
