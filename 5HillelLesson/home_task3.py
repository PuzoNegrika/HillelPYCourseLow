import string

s = input("Введіть рядок, для перетворення в hashtag: ")


clean_s = ''.join(p for p in s if p not in string.punctuation)
words = clean_s.split()
hashtag = '#' + ''.join(word.capitalize() for word in words) # тут я питав у ШІ: як зробити першу літеру рядка на велику, а інші - малими. Сказав користуватись capitalize()
hashtag = hashtag[:140]

print(hashtag)