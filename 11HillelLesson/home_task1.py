from inspect import isgenerator
# isgenerator - перевіряє, чи є об’єкт генератором

def prime_generator(end):
    for num in range(2, end+1): # переберу усі числа від 2 до end ВКЛЮЧНО
        for i in range(2, num): # перевірка на те, що ділиться num на будь-яке число від 2 до num НЕ ВКЛЮЧНО
            if num % i == 0:
                break
        else:
            yield num

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')


# для себе про yield
def count_up_to(n):
    for i in range(1, n+1):
        yield i  # повертає по одному числу, при цьому зберігає минулий результат

gen = count_up_to(3)
print(list(gen))
# Коли робимо next(gen), вона дає перше число 1, зберігає його стан, а потім наступний next(gen) дає 2 і так далі

