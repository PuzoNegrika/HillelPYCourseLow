def common_elements():
    set1 = {x for x in range(100) if x % 3 == 0}
    set2 = {x for x in range(100) if x % 5 == 0}
    return set1 & set2

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')