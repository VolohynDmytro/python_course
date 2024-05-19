def popular_words(text: str, words: list) -> dict:
    text = text.lower()
    text_list = text.split()
    counted_dict = {}
    for elem in words:
        count = text_list.count(elem.lower())
        counted_dict[elem] = count
    return counted_dict


if __name__ == "__main__":
    assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                         ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
    print('OK')
