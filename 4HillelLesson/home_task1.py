lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

#      [нове_значення for елемент in список if умова]
zero_lst = [x for x in lst if x != 0]
zeros = lst.count(0)
lst = zero_lst + [0] * zeros
print(lst)