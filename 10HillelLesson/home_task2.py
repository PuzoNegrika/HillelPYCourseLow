def first_word(text):
    """ Пошук першого слова """
    i = 0
    while i < len(text) and text[i] in " .,":
        i += 1

    word = ""
    while i < len(text) and (text[i].isalpha() or text[i] == "'"):
        word += text[i]
        i += 1

    return word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')