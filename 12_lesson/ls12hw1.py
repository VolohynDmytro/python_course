import codecs
from bs4 import BeautifulSoup as Bs


def delete_html_tags(html_file: str, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        soup = Bs(html, features="html.parser")
        with open(result_file, 'at') as fl:
            for strings in soup.stripped_strings:
                fl.writelines(f'{repr(strings)}\n')
            print(file.read())
            file.close()


delete_html_tags('draft.html')
