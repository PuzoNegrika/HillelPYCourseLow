def is_even(number):
    bitn = number & 1
    if bitn == 0:
        return True
    else:
        return False

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("Ok")
# Бо якщо останній біт - 1, то це False, а якщо 0 - True. Типу парне/не парне, якщо я правильно зрозумів