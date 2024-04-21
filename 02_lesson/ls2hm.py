



num_input = input('!!!!!Введите целое 4-х значное число:  ')

a = int(num_input)
b = a//1000
print(b)

c = a//100
d = c - b*10
print(d)

e = a//10
f = e - c*10
print(f)

g = a//1 - e*10
print(g)