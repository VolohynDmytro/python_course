import copy
import math

ls1 = [111, 222, 333, 4444, 5555, 6666]

splitter = len(ls1)/2

if splitter != int:
    splitter = math.ceil(splitter)
    firstLs = copy.deepcopy(ls1[:splitter])
    secondLs = copy.deepcopy(ls1[splitter:])
    finalLS = [firstLs, secondLs]
    print(finalLS)

else:
    firstLs = copy.deepcopy(ls1[:splitter])
    secondLs = copy.deepcopy(ls1[splitter:])
    finalLS = [firstLs, secondLs]
    print(finalLS)



ls2 = [111, 222, 333, 4444, 5555]

splitter = len(ls2) / 2

if splitter != int:
    splitter = math.ceil(splitter)
    firstLs = copy.deepcopy(ls2[:splitter])
    secondLs = copy.deepcopy(ls2[splitter:])
    finalLS = [firstLs, secondLs]
    print(finalLS)

else:
    firstLs = copy.deepcopy(ls2[:splitter])
    secondLs = copy.deepcopy(ls2[splitter:])
    finalLS = [firstLs, secondLs]
    print(finalLS)



ls3 = [111]

splitter = len(ls3) / 2

if splitter != int:
    splitter = math.ceil(splitter)
    firstLs = copy.deepcopy(ls3[:splitter])
    secondLs = copy.deepcopy(ls3[splitter:])
    finalLS = [firstLs, secondLs]
    print(finalLS)

else:
    firstLs = copy.deepcopy(ls3[:splitter])
    secondLs = copy.deepcopy(ls3[splitter:])
    finalLS = [firstLs, secondLs]
    print(finalLS)



ls4 = []

splitter = len(ls4) / 2

if splitter != int:
    splitter = math.ceil(splitter)
    firstLs = copy.deepcopy(ls4[:splitter])
    secondLs = copy.deepcopy(ls4[splitter:])
    finalLS = [firstLs, secondLs]
    print(finalLS)

else:
    firstLs = copy.deepcopy(ls4[:splitter])
    secondLs = copy.deepcopy(ls4[splitter:])
    finalLS = [firstLs, secondLs]
    print(finalLS)





