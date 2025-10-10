lst = [1, 2, 3, 4, 5, 6] # len(lst) = 6

if len(lst) == 0:
    result  = [[], []]
elif len(lst) % 2 == 0:
    middle = len(lst) // 2 # парна
    result = [lst[:middle], lst[middle:]]
else:
    middle = len(lst) // 2 + 1 # не парна
    result = [lst[:middle], lst[middle:]]

print(result)