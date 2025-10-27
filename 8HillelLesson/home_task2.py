def is_palindrome(text):
    clean_text = ''
    for x in text:
        if x.isalnum():
            clean_text += x.lower()
            # Маю текст без пробілів і знаків пунктуації
    if clean_text == clean_text[::-1]:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")