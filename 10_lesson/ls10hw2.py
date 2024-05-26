def first_word(text: str) -> str:
    for symbol in text:
        if not symbol.isalpha() and symbol != ' ' and symbol != "'":
            text = text.replace(symbol, ' ')
    word_list = text.split()
    searching_word = word_list[0]
    if not searching_word[-1].isalpha():
        return searching_word[:-1]
    else:
        return searching_word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
