def say_hi(name, age):
  return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')
# assert - це перевірка, яку Python робить під час виконання коду. Він порівнює, чи результат дорівнює тому, що ми очікуємо. Якщо ж перевірка проходить - програма йде далі, а якщо ні - зупиняю програму і показує помилку.