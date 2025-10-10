lst = [0, 1, 7, 2, 4, 8, 3, 5]
print(len(lst))

if len(lst) == 0:
    result = 0
else:
    sum_even_idx = sum(lst[::2])
    result = sum_even_idx * lst[-1]  # множимо тут на останній елемент у списку
print(result)
