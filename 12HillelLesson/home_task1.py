import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
          html = file.read()

    result = re.sub(r'<.*?>', '', html) # сам пайчарм підказав, але я можу зробити з циклом, по типу: for char in html, якщо це рішення не правильне

    with open (result_file, 'w', encoding='utf-8') as f:
        f.write(result)