x = float(input("Введіть перше число: "))
y = input("Введіть дію, яка буде виконуватися над цими числами (+, -, *, /): ")
z = float(input("Введіть друге число: "))

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    if z == 0:
        print("Помилка: дільник не може дорівнювати нулю!")
    else:
        print(x / z)
else:
    print("Помилка: перевірте данні!")