import string
import keyword

s = input("Введіть рядок, який міг би бути ім'ям змінної: ")


if s[0].isdigit():
    print("False, ім'я змінної не може починатися з цифри!")
elif any(w.isupper() for w in s):
    print("False, ім'я змінної не може містити в собі великі літери!")
elif any(p in string.punctuation and p != "_" for p in s) or " " in s:
    print("False, ім'я змінної не може містити пробіл і знаки пунктуації в собі!")
elif s in keyword.kwlist:
    print("False, ім'я змінної не може бути вже зареєстрованним словом!")
elif any(s[i] == s[i+1] == '_' for i, _ in enumerate(s[:-1])): # змінив, але трішки за допомогою ШІ
    print("False, ім'я змінної не може містити два підряд '_'!")

else:
    print("True, ім'я змінної допустимо!")