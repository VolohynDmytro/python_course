def correct_sentence(text: str) -> str:
    str_list = list(text)
    str_list[0] = str_list[0].upper()
    if str_list[-1] == '.':
        pass
    else:
        str_list.append('.')
    corrected_str = ''.join(str_list)
    return corrected_str


print(correct_sentence("hello"))

assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
print('ОК')
