lst = [0, 1, 7, 2, 4, 4, 2, 5]
print(len(lst))

if len(lst) == 0:
    result = 0
elif len(lst) % 2 == 0:
    sum_even_idx = sum(lst[::2])
    result = sum_even_idx * lst[-1]  # множимо тут на останній елемент у списку
print(result)
