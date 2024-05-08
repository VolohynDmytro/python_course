inp = input('Cifra: ')

if int(inp) > 9:
    inp = list(map(int, inp))
    print(inp)
    start_point = inp.pop(0)
    for number in range(len(inp)):
        start_point = start_point * inp[number]
    inp = start_point
    print(inp)
    while inp > 9:
        inp = list(map(int, str(inp)))
        print(inp)
        start_point = inp.pop(0)
        for number in range(len(inp)):
            start_point = start_point * inp[number]
        inp = start_point
        print(inp)
else:
    print(inp)
