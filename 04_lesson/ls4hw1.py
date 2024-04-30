base_list = [0, 15, 0, 98, 0, 956, 0]

print(base_list)

for elem in base_list:
    if elem == 0:
        base_list.remove(elem)
        base_list.append(elem)
print(base_list)
