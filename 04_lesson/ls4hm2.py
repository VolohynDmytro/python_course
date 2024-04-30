base_list = [15, 98, 0, 956, 0, 99, 0, 0, 45]

print(base_list)
result = 0

for index in range(len(base_list)):
    if not index % 2:
        result = result + base_list[index]

result = result*base_list[-1]

print(result)
