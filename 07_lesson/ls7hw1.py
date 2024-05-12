def say_hi(name: str, age: int) -> str:
    hi_string = f"Hi. My name is {name} and I'm {age} years old"
    print(hi_string)
    return hi_string


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
print('ОК')
