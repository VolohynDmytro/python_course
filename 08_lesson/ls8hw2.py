def is_palindrome(text: str) -> bool:
    right_string = ''.join(symb for symb in text if symb.isalpha() or symb.isdigit())
    right_string = right_string.casefold()
    if right_string == right_string[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('0P') == False
    assert is_palindrome('a.') == True
    assert is_palindrome('aurora') == False
    print("ОК")
