x = int(input("Введіть ціле число: "))

while x > 9:
    res = 1
    for digit in str(x):
        res = res * int(digit)
    x = res
print(x)