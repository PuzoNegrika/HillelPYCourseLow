import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
          html = file.read()

    result = ''
    tag = False

    for char in html:
        if char == '<':
            tag = True
        elif char == '>':
            tag = False
        elif not tag:
            result += char

    with open(result_file, 'w', encoding='utf-8') as f:
        f.write(result)