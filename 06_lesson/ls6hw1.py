import string

input_str = input('Введи две английские буквы через дефис "-" ')

start, end = input_str.split('-')
base_str = string.ascii_letters

print(base_str)

start_index = base_str.index(start)
end_index = base_str.index(end)

print(base_str[start_index:end_index+1])
