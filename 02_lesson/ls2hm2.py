



num_input = input('!!!!!Введите целое 5-и значное число:  ')

a = int(num_input)
b = a//10000

c = a//1000
d = c - b*10


e = a//100
f = e - c*10

g = a//10
h = a//10 - e*10


i = a//1 -g*10

res = i*10000+h*1000+f*100+d*10+b
print(res)