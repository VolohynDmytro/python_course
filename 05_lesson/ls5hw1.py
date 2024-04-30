import keyword
from string import punctuation

string = input("Введите название для переменной: ")

for i in range(len(string)):
    if string[i].isupper():
        print(f'{string} => False')
        exit()
for i in range(len(string)):
    if punctuation.find(string[i]) >= 0 and punctuation.find(string[i]) != 26:
        print(f'{string} => False')
        exit()
for i in range(len(string)):
    if string[i].isspace():
        print(f'{string} => False')
        exit()
for elem in range(len(keyword.kwlist)):
    if string.find(keyword.kwlist[elem]) >= 0 and string.isalnum():
        print(f'{string} => False')
        exit()
if not string[0].isdigit():
    print(f'{string} => True')
else:
    print(f'{string} => False')
    exit()
