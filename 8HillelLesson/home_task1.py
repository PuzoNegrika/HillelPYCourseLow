def add_one(some_list):
    num = ''
    for item in some_list:
        num += str(item)
    num_int = int(num) + 1
    result = []
    for d in str(num_int):
        result.append(int(d))
    return result

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")