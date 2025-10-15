import string
import keyword

s = input("Введіть рядок, який міг би бути ім'ям змінної: ")


if set(s) == {"_"}: # я тут також шукав і питав у ШІ, яку треба ф-цію, щоб вона брала елементи, без повторів - set()
    if len(s) == 1:
        print("True, ім'я змінної допустимо!")
    else:
        print("False, ім'я змінної не може мати в собі більше ніж 1 елемент '_'!")
elif s[0].isdigit():
    print("False, ім'я змінної не може починатися з цифри!")
elif any(w.isupper() for w in s):
    print("False, ім'я змінної не може містити в собі великі літери!")
elif any(p in string.punctuation and p != "_" for p in s) or " " in s:
    print("False, ім'я змінної не може містити пробіл і знаки пунктуації в собі!")
elif s in keyword.kwlist:
    print("False, ім'я змінної не може бути вже зареєстрованним словом!")

else:
    print("True, ім'я змінної допустимо!")