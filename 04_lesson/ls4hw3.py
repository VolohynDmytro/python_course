from random import randint

base_list = []

for elem in range(3, randint(4, 10)):
    base_list.append(randint(0, 10))
print(base_list)
new_list = [base_list[0], base_list[2], base_list[-2]]
print(new_list)
