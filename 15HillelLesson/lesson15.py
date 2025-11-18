# Способи керування доступом до полів класу.
# Методи які використовуються для маніпулювання атрибутами об'єктів класу:  !!!
# 1 - Метод __getattribute__ - викликається автоматично при спробі набути значення певного або невизначеного (відсутнього) поля класу
# 2 - Метод __getattr__ - викликається автоматично при спробі отримати значення невизначеного поля класу
# 3 - Метод __setattr__ - викликається при спробі надати значення будь-якому полю класу (певного та невизначеного)
# 4 - Метод __delattr__ – викликається при видаленні поля


# Метод __getattr__.
# !!! Метод __getattr__ - автоматично викликається інтерпретатором під час спроби одержати значення невизначених полів класу
# Тобто, полів, які відсутні у класі і були прикріплені до об'єкту після його створення
# Для певних полів класу (тобто ті які можуть бути виявлені інтерпретатором у результаті висхідного пошуку) цей метод не викликається.
#
# Синтаксис його реалізації такий:
# __getattr__ (self, attrname)
# де: self — посилання на об'єкт для якого відбувається звернення до невизначеного поля, а attrname — назва поля

# Стандартна поведінка. При зверненні до поля якого немає код викликає помилку AttributeError:
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color = {}]"
        return msg.format(self.name, self.age, self.color)


cat = Cat('Barsik', 3, 'black')
print(cat.name) # Barsik
## print(cat.type) # AttributeError Звернення до поля, якого немає

# Якщо ми перевизначимо метод __getattr__, то зможемо погасити помилку:
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color = {}]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        return None # pass

cat = Cat('Barsik', 3, 'black')
print(cat.name)  # виведе Barsik

# Звернення до поля, якого немає
print(cat.type)  # виведе  None
print()


# Метод getattr().
# !!! Функція getattr() в Пайтон - це вбудована функція, яка дозволяє отримати значення атрибута об'єкта за його ім'ям, яке задається рядком
# !!! Атрибутом може бути змінна, метод, властивість або будь-який інший елемент, який належить об'єкту
# !!! Функція getattr() приймає три параметри: об'єкт, ім'я атрибута і значення за замовчуванням, яке повертається, якщо атрибут не знайдено
# Синтаксис функції getattr() такий: getattr(object, name, default=None):
cat = Cat('Barsik', 3, 'black')
print(getattr(cat, "name")) # виведе Barsik
print(getattr(cat, "age")) # виведе 3
print(getattr(cat, "color")) # виведе black

# За допомогою getattr можна отримувати будь-який атрибут об'єкта, наприклад це може бути функція:
import math
pow_math = getattr(math, 'pow')
print(pow_math(4, 2)) # виведе 16

# Якщо ви спробуєте отримати значення неіснуючого атрибута, ви отримаєте виняток AttributeError, якщо не вказали значення за замовчуванням. Наприклад:
## print(getattr(math, 'okras')) # AttributeError

# Але якщо ви вкажете значення за замовчуванням, наприклад, None, ви отримаєте це значення замість винятку. Наприклад:
print(getattr(math, 'piii', None)) # виведе None

# Використовуючи гетатр можна динамічно отримувати значення з об'єкта, не вдаючись до точкової нотації:
cat = Cat('Barsik', 3, 'black')
fields = ['age', 'name', 'color']
for field in fields:
    print(getattr(cat, field))
print()


# hasattr().
# !!! Функція hasattr() в Пайтон - це вбудована функція, яка дозволяє перевірити, чи має об'єкт певний атрибут, який задається рядком
# !!! Атрибутом може бути змінна, метод, властивість або будь-який інший елемент, який належить об'єкту
# !!! Функція hasattr() приймає два параметри: об'єкт і ім'я атрибута, і повертає True, якщо об'єкт має такий атрибут, і False, якщо ні
# Синтаксис функції hasattr() такий: hasattr(object, name)
# Наприклад, якщо ви маєте клас Cat з атрибутами name, age і color, ви можете перевірити, чи має він певні атрибути так:
cat = Cat('Barsik', 3, 'black')
print(hasattr(cat, "name")) # виведе True
print(hasattr(cat, "age")) # виведе True
print(hasattr(cat, "color")) # виведе True
print(hasattr(cat, "gender")) # виведе False
print()


# Метод __getattribute__.
# !!! Метод повинен повернути обчислене значення для зазначеного атрибуту, або підняти виняток AttributeError
# !!! Метод __getattribute__ автоматично викликається інтерпретатором при отриманні будь-якого поля
# !!! Через цього працювати з таким методом особливо складно, оскільки великий ризик попадання у нескінченний рекурсивний виклик
# !!! Це відбувається тому, що спроба звернення з цього методу до будь-якого з полів (навіть до __dict__) призводить до його повторного виклику
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color = {}]"
        return msg.format(self.name, self.age, self.color)

    def __getattribute__(self, atr_name):
        """ Робити перехоплення винятку у цьому методі, не
				зовсім коректно.
        Більш правильний підхід - реалізувати роботу з полями,
        яких немає, у методі __getattr__"""
        try:
            return object.__getattribute__(self, atr_name)
        except AttributeError:
            return None

cat = Cat('Barsik', 3, 'black')
print(cat.name)  # виведе Barsik

# Звернення до поля, якого немає
print(cat.type)  # виведе  None
# Якщо крім цього методу для класу також визначено __getattr__, він буде викликаний у двох випадках:
# 1 - Якщо __getattribute__ підніме виняток AttributeError
# 2 - Якщо __getattribute__ викличе його явно
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        return None

    def __getattribute__(self, atr_name):
        return object.__getattribute__(self, atr_name)

cat = Cat('Barsik', 3, 'black')

print(cat.name)  # виведе Barsik

# Звернення до поля, якого немає
print(cat.type)  # виведе  None
print()


# Метод встановлення значень поля __setattr__.
# !!! Метод __setattr__ автоматично викликається інтерпретатором під час встановлення значення будь-якого поля
# !!! Робота з таким методом також може бути проблематичною тому, що цей метод викликається при спробі встановлення будь-якого поля
# !!! Як і у випадку з методом __getattribute__, це може призвести до нескінченного рекурсивного виклику
# !!! Однак, ця проблема вирішується набагато простіше - достатньо виконати запис у вже існуюче поле __dict__
#
# !!! Примітним фактом є те, що цей метод викликається навіть під час роботи конструктора (метод __init__)
# !!! Таким чином цей метод викликається і при ініціалізації об'єкта та при спробі присвоєння значення будь-якому полю:
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        if atr_name == "type":
                return "Home Cat"
        print(atr_name)
        return "11"

    def __getattribute__(self, atr_name):
        return object.__getattribute__(self, atr_name)

    def __setattr__(self, attr_name, attr_value):
        self.__dict__[attr_name] = attr_value

cat = Cat('Barsik', 3, 'black')

cat.type =  "Devil"
print(cat.type)   # виведе Devil
print()


# Функція setattr().
# !!! Функція setattr() в Пайтон - це вбудована функція, яка дозволяє встановити значення атрибута об'єкта за його ім'ям, яке задається рядком
# !!! Атрибутом може бути: змінна, метод, властивість або будь-який інший елемент, який належить об'єкту
# !!! Функція setattr() приймає три параметри: об'єкт, ім'я атрибута і значення, яке потрібно присвоїти атрибуту
# !!! Синтаксис функції setattr() такий: setattr(object, name, value)
cat = Cat('Barsik', 3, 'black')
setattr(cat, "name", "Bob") # змінює ім'я на Bob
setattr(cat, "age", 5) # змінює вік на 5
setattr(cat, "color", "red") # змінює колір на red
print(cat)  # виведе Cat [ name = Bob, age = 5, color = red]

# !!! Функція setattr() в Пайтон корисна, коли ви хочете динамічно встановлювати атрибути об'єктів, які не відомі наперед, або коли ви хочете створювати або змінювати атрибути у об'єктів на льоту
dct = {'name': "Voland", "age": 45, "color": "black"}
for key, val in dct.items():
    # Встановимо нові значення для полів об'єкта
    setattr(cat, key, val)

print(cat)  # виведе Cat [ name = Voland, age = 45, color = black]
print()


# Метод __delattr__.
# !!! Метод __delattr__ викликається у разі спроби видалення будь-якого поля
# !!! Як і в у разі методу __setattr__ потрібно вжити заходів щодо запобігання нескінченному рекурсивний виклик
# !!! Це можна реалізувати або за допомогою делегування цієї операції суперкласу, або використовуючи словник __dict__
# !!! Сигнатура методу __delattr__ така: __delattr__ (self, attr_name), де self — посилання на об'єкт, attr_name — ім'я поля у вигляді рядка
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color ={}]"
        return msg.format(self.name, self.age, self.color)

    def __getattr__(self, atr_name):
        if atr_name == "type":
                return "Home Cat"
        print(atr_name)
        return "11"

    def __getattribute__(self, atr_name):
        return object.__getattribute__(self, atr_name)

    def __setattr__(self, attr_name, attr_value):
        print("set field -> ", attr_name)
        self.__dict__[attr_name] = attr_value

    def __delattr__(self, attr_name):
        # Видаляємо поле з внутрішньої структури об'єкта
        print("remove field ", attr_name)
        del self.__dict__[attr_name]

cat = Cat('Barsik', 3, 'black')
cat.type =  "Devil"
del cat.type
print()


# Властивості property.
# Методи __getattr__, __setattr__, __getattribute__ та __delattr__ дозволяють керувати загальним доступом до полів класу
# Тобто, вони викликаються під час звернення до будь-якого полю
# Якщо ж потрібно керувати доступом к кожному полю індивідуально, то для цього може використовувати протокол властивостей (property)
#
# !!! Протокол властивостей дозволяє спрямовувати операції читання та запису для окремих полів, функціям та методам, що дозволяє додавати програмний код, який буде викликатись автоматично при спробах звернення до поля
# З погляду інформатики властивість - спосіб доступу до внутрішнього стану об'єкта, що імітує змінну певного типу
# !!! Звернення до властивості об'єкта виглядає так само, як і звернення до звичайного поля, але насправді реалізовано через виклик функції
# !!! При спробі поставити значення цієї властивості викликається один метод, а при спробі отримати значення цієї властивості — інший
# !!! В Python властивості створюються за допомогою вбудованої функції property і надаються атрибутам класів, так само, як виконується надання функцій методам
#
# Вбудована функція property
# !!! property() в Пайтон - це вбудована функція, яка дозволяє створювати атрибути класу з гетерами, сетерами і делетерами:  !!!
# Гетер - це метод, який повертає значення атрибуту
# Сетер - це метод, який змінює значення атрибуту
# Делетер - це метод, який видаляє атрибут
# !!! Атрибути класу в Python — це змінні, які зберігають дані для всіх об'єктів (екземплярів) певного класу

# !!! property() приймає чотири необов'язкових параметри: fget, fset, fdel і doc, які відповідають гетеру, сетеру, делетеру і документації атрибуту відповідно
# property() повертає об'єкт класу property, який можна використовувати для контролю доступу до атрибуту
# Сигнатура цієї функції така: property(f_get, f_set, f_del, doc), де:  !!!
# 1 - f_get - функція або метод викликана при читанні значення поля
# 2 - f_set — функція або метод, що викликається при встановленні значення поля
# 3 - f_del — функція або метод, що викликається при видаленні поля
# 4 - doc - рядок документування з описом поля
# !!! Всі ці параметри можуть бути опущені і за промовчанням дорівнюють None
class Cat:
    def __init__(self, _name, age):
        self.__name = _name   # захищене поле
        self.age = age

    def get_name(self): # Метод для читання
        print("call get name")
        return self.__name

    def set_name(self, name_value): # Метод для запису
        print("call set name")
        self.__name = name_value

    def del_name(self): # Метод видалення
        print("call remove name")
        del self.__name

    # Створення властивості name
    name = property(get_name, set_name, del_name, " Cat name")

    def __str__(self):
        msg = "Cat [ name = {}, age = {}]"
        return msg.format(self.name, self.age)

cat1 = Cat("Vaska", 6)
cat1.name = "Barsic"  # буде викликаний метод set_name
print(cat1.name)  # буде викликаний метод get_name
print(cat1)

# Визначення властивостей за допомогою декораторів
# !!! Декоратор — це структурний патерн, який дозволяє додавати "на льоту" нові поведінки об'єктам, розміщаючи їх в об'єктах-обгортках
# !!! Функція property може приймати лише один перший аргумент (Інші за замовчуванням None) і повертати властивість
# !!! Властивість у свою чергу є об'єктом, що викликається, оскільки при зверненні до нього викликаються функції
# !!! Це означає, що функцію property можна використовувати як декоратор визначення функції отримання значення поля
# !!! У свою чергу об'єкти властивостей мають методи getter, setter, deleter. Які у свою чергу повертають також властивість додавши до нього методи доступу
# Як наслідок, ці методи також можна використовувати як декоратори:
# 1 - getter - отримання значення поля
# 2 - setter - встановлення значення поля
# 3 - deleter - видалення поля
# !!! Увага! Важливо, щоб усі методи до яких ви хочете застосувати перераховані вище декоратори носили ім'я властивості
class Cat:
    def __init__(self, _name, age):
        self.__name = _name
        self.age = age

    name = property() # Створення властивості name без методів контролю

    @name.getter
    def name(self):
        print("call get name")
        return self.__name

    @name.setter
    def name(self, name_value):
        print("call set name")
        self.__name = name_value

    @name.deleter
    def name(self):
        print("call remove name")
        del self.__name

cat = Cat('Barsik', 3)
print(cat.name)  # getter
cat.name =  "Devil" # setter
del cat.name  # deleter

# !!! Якщо не визначити методи встановлення значення та видалення, тоді таке поле стане рід-онлі
class Cat:
    def __init__(self, _name, age):
        self.__name = _name
        self.age = age

    @property
    def name(self):
        return self.__name

cat = Cat('Barsik', 3)
print()
## cat.name =  "Devil" # AttributeError: can't set attribute
## del cat.name # AttributeError: can't delete attribute

# !!! Спрощений варіант застосування property. За допомогою property можна перетворити функцію в звичайне поле
# !!! Тобто в результаті ми отримуємо поле, яке обчислюється щоразу, коли ми до нього звертаємось
class Human:

    def __init__(self, last_name, first_name, patronymic, gender, age, height, weight):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight

    def show_inform(self):
        full_name = f'Full Name: {self.full_name}\n'
        gender_age = f'Gender: {self.gender}\nAge: {self.age}\n'
        height_weight = f'Height: {self.height} cm\nWeight: {self.weight} kg'
        all_info = full_name + gender_age + height_weight
        return all_info

    @property  #cashed_property
    def full_name(self):
        # Перетворення функції (методу) у звичайне поле
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    @property
    def short_full_name(self):
        return f'{self.last_name} {self.first_name[0].title()}.{self.patronymic[0].title()}.'

h = Human('Лучко', 'Петро', 'Петрович', 'male', 25, 185, 91)

print(h.full_name) # Лучко Петро Петрович
print(h.short_full_name) # Лучко П.П.
print(h.last_name) # Лучко

print(h.show_inform())  # звернення до методу
print()


# Дескриптори та методи доступу.
# Дескриптори.
# Дескриптори забезпечують альтернативний варіант управління полями
# І хоча схожий механізм надають property, дескриптори, здатні надати багатший функціонал
# !!! З технічної точки зору property є окремим випадком дескрипторів. Функція property просто спрощує процес створення дескриптора певного типу
#
# !!! Дескриптори здатні передати виконання операцій отримання та встановлення значень, окремим методам об'єктів спеціально створених для цього класів
# !!! Дескриптори створюються як окремі класи. Об'єкти цих класів присвоюються під час створення керованих полів класів
# !!! Це має певну перевагу, тому що об'єкти класів дескрипторів здатні зберігати значення, яких немає в класах, в яких вони будуть використані
# Однак це ж додає найбільш складний аспект при їх використанні, необхідність передачі посилання на об'єкт використовує дескриптори та посилання на сам об'єкт дескриптора

# Створення дескриптора
# !!! Для створення дескриптора потрібно створити клас, в якому будуть реалізовані такі методи:  !!!
# 1 - Для отримання значення __get__(self, instance_self, instance_class) self — посилання на об'єкт дескриптора, instance_self — посилання на об'єкт, який використовує поля керовані дескриптором, instance_class — клас до якого прикріплено поле кероване дескриптором
# 2 - Для встановлення значення __set__(self, instance_self, value) instance_self — посилання на об'єкт, який використовує поля керовані дескриптором, value - нове значення
# 3 - Для видалення __delete__(self, instance_self)
# !!! Будь-який клас, де реалізовані ці методи є дескриптором.
# У разі відсутності реалізації того чи іншого методу, ця операція просто не підтримуватиметься


# Гетер.
# Метод __get__ приймає наступний ряд параметрів: __get__(self, instance_self, instance_class), де:  !!!
# 1 - self — посилання на об'єкт дескриптора
# 2 - instance_self — посилання на об'єкт, який використовує поля керовані дескриптором. Якщо до поля виконано звернення через ім'я класу, цей параметр дорівнює None
# 3 - instance_class — клас до якого прикріплено поле кероване дескриптором
class Coordinate:

    def __init__(self, val):
        self.value = val

    def __get__(self, instance, owner):
        return self.value

class Point:
    x = Coordinate(10)
    y = Coordinate(12)

point = Point()
print(point.x)  #  виведе 10
print(point.y)  #  виведе 12
# У разі відсутності реалізації методу __set__ перша спроба встановити значення такого поля просто замінить дескриптор. По суті, просто відключить його
point.x = 4
print(point.x) # виведе 4, а мало бути 10
print()


# Сетер.
# Метод set приймає наступний ряд параметрів __set__(self, instance_self, value), де:  !!!
# 1 - self — посилання на об'єкт дескриптора
# 2 - instance_self — посилання на об'єкт, який використовує поля керовані дескриптором. Якщо до поля виконано звернення через ім'я класу, цей параметр дорівнює None
# 3 - value — значення, яке потрібно привласнити полю
# !!! Щоб зробити поле доступним лише для читання з використанням дескриптора, потрібно реалізувати метод __set__ дескриптора, де порушити виняток
# У такому разі при спробі зміни поля буде порушено виняток
class Coordinate:

    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

class Point:
    x = Coordinate()
    y = Coordinate()

point = Point()
print(point.x, point.y) # виведе None None
point.x = 50
point.y = 20
print(point.x, point.y) # виведе 50 20
print()


# Делітер.
# Про реалізацію методу __delete__ дескриптора
# Метод __delete__ приймає наступний ряд параметрів __delete__(self, instance_self), де:  !!!
# 1 - self — посилання на об'єкт дескриптора
# 2 - instance_self — посилання на об'єкт, який використовує поля керовані дескриптором. Якщо до поля виконано звернення через ім'я класу, цей параметр дорівнює None
class Coordinate:

    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

    def __delete__(self, instance):
        del self.value

class Point:
    x = Coordinate()
    y = Coordinate()

point = Point()
point.x = 50
point.y = 20
print(point.x, point.y)  # виведе 50 20

del point.x
## print(point.x) # AttributeError: 'Coordinate' object has no attribute 'value'

# Приклад реалізації дескриптора для поля, яке має бути більше за 0:
class PositiveValue:

    def __init__(self):
        self.val = None

    def __get__(self, instance_self, instance_class):
        return self.val

    def __set__(self, instance_self, value):
        if value < 0:
            raise ValueError('Value must be greater than zero')
        self.val = value

class Box:
    x = PositiveValue()
    y = PositiveValue()
    z = PositiveValue()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

box = Box(1, 2, 3)
print(box.x) # виведе 1

## box.x = -1  # ValueError
## box = Box(1, 2, -3)  # ValueError
print()


# Ітераційний протокол та робота з ітераторами.
# Ітератори та ітераційний протокол.
# !!! Щоб екземпляр користувальницького класу, міг виконувати роль послідовності, потрібна реалізація двох наступних методів або, як ще кажуть, реалізувати інтерфейс послідовностей:
# __getitem__(self, index) - "Магічний" метод, який перевизначає отримання елемента за індексом
# __len__(self) - "Магічний" метод, який повертає довжину послідовності
class UserSequence:
    """Реалізація послідовності квадратів чисел
    """
    def __init__(self, number):
        self.number = number

    def __getitem__(self, index):
        if index < self.number:
            return index ** 2 # поверне квадрат значення index
        else:
            raise IndexError

    def __len__(self):
        return self.number

seq = UserSequence(10)
# Отримуємо елементи послідовності у циклі
for i in range(len(seq)):
    print(seq[i], end=', ') # виведе 0, 1, 4, 9, 16, 25, 36, 49, 64, 81,

# Можемо отримати елемент послідовності за індексом
print(seq[9]) # виведе 81

# Можемо отримати всі елементи послідовності у вигляді списку
print(list(seq))  # виведе [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print()

# Спроба отримати зріз, як у звичайному об'єкті, що ітерується, приведе до помилки
## print(seq[2: 4]) # TypeError: '<' not supported between instances of 'slice' and 'int' (Python передає в метод __getitem__ не число, а об’єкт типу slice)


# Об'єкти зрізу slice().
# !!! Функція slice() в Пайтон - це вбудована функція, яка повертає об'єкт срізу, який можна використовувати для отримання підпослідовностей з рядків, списків, кортежів та інших ітерабельних об'єктів
# !!! Функція slice() приймає три параметри: start, stop і step, які визначають початок, кінець і крок срізу
# !!! Наприклад: якщо ви маєте рядок s = "Hello World", то ви можете отримати сріз s[1:3], який поверне "el"
#
# !!! Ви також можете використовувати функцію slice() для створення об'єкта срізу, який можна передати іншим функціям або зберегти для подальшого використання
# !!! Наприклад: ви можете створити об'єкт срізу sl = slice(1, 3) і потім використовувати його для отримання срізів з різних рядків, таких як s[sl] або "Hello World"[sl]
some_slice = slice(0, 3)
print(some_slice.start)  # виведе 0
print(some_slice.stop)  # виведе 3
print(some_slice.step)  # виведе None

a = [5, 6, 7, 8, 9]
print(a[some_slice]) # виведе [5, 6, 7], а не [6, 7, 8]
print(a[0:3]) # виведе [5, 6, 7]

print(a[slice(None, None, 2)]) # [5, 7, 9], [None, None] = [::]
print(a[::2]) # [5, 7, 9], тобто ці 2 рядки однакові !!!

print(a[slice(None)]) # [5, 6, 7, 8, 9]
print(a[::]) # [5, 6, 7, 8, 9] # від початку, до кінця, по типу як і: [:]

print(a[slice(None, None, -1)]) # [9, 8, 7, 6, 5]
print(a[::-1])

# Виправимо клас послідовності таким чином, щоб отримувати список при зверненні за допомогою зрізів:
class UserSequence:
    """ Реалізація послідовності квадратів чисел, що підтримує звернення за допомогою зрізів"""

    def __init__(self, number):
        self.number = number

    def __getitem__(self, index):
        # перевірка того, що індекс це об'єкт зрізу
        if isinstance(index, slice):
            # перевірка коректності значень об'єкт зрізу
            if index.start and index.start < 0:
                raise IndexError
            elif index.stop and index.stop > self.number:
                raise IndexError
            result = []
            # встановлення конкретних значень зрізу, якщо такі не були задані
            start = 0 if index.start is None else index.start
            stop = self.number if index.stop is None else index.stop
            reverse = False
            # якщо значення кроку від'ємне, значить буде перевернута послідовність
            if index.step and index.step < 0:
                reverse = True
                step = index.step * (-1)
            else:
                step = 1 if index.step is None else index.step
            # процес формування послідовності
            for i in range(start, stop, step):
                result.append(i ** 2)
            # перевертаємо послідовність, якщо reverse = True
            return list(reversed(result)) if reverse else result

        if isinstance(index, int):
            if index < self.number:
                return index ** 2
            else:
                raise IndexError
        raise TypeError

    def __len__(self):
        return self.number

seq = UserSequence(10)
print(seq[1:8])  # [1, 4, 9, 16, 25, 36, 49]
print(seq[:10:2])  # [0, 4, 16, 36, 64]
print(seq[:])  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(seq[::-1])  # [81, 64, 49, 36, 25, 16, 9, 4, 1, 0]
print()
# isinstance() - вбудована функція для перевірки, чи є об'єкт екземпляром зазначеного класу чи кортежу класів. Вона повертає True, якщо об'єкт належить до класу (або одного з класів у кортежі), і False інакше. Функція корисна для перевірки типів даних, валідації та забезпечення безпечних операцій
# Синтаксис: isinstance(object, classinfo), де:
# object — об'єкт, тип якого ви хочете перевірити
# classinfo — клас, тип або кортеж із класів, за якими проводиться перевірка


# Ітератори.
# !!! Ітератор (від англ. iterator - перечислювач) - інтерфейс, що надає доступ до елементів колекції (масиву або контейнера) та навігацію по них
#
# iter(), next()
# !!! Функції iter() та next() в Пайтон - це вбудовані функції, які дозволяють працювати з ітераторами
# !!! Ітератор - це об'єкт, який може повертати свої елементи по одному за допомогою методу next()
# !!! Ітератори використовуються для обходу різних колекцій, таких як списки, рядки, словники, множини тощо
#
# !!! Функція iter() приймає якийсь ітерабельний об'єкт, наприклад список, і повертає ітератор для цього об'єкта
# !!! Функція next() приймає якийсь ітератор і повертає наступний елемент з нього. Якщо елементів більше немає, то функція викликає виняток StopIteration
# Функції iter() та next() дуже корисні для реалізації власних ітераторів або генераторів, які можуть виробляти послідовності значень за вимогою
lst = [1, 2, 3, 4, 5]
it = iter(lst)
# it - це ітератор для списку lst
print(type(it)) # <class 'list_iterator'>
print(next(it)) # виведе 1
print(next(it)) # виведе 2
print(next(it)) # виведе 3
print(next(it)) # виведе 4
print(next(it)) # виведе 5
## print(next(it)) # викличе виняток StopIteration

# Усі вбудовані типи даних мають свій ітератор, який знає, як потрібно працювати з цим типом даних
a = "Hello"
b = a.__iter__()
print(type(b)) # виведе: <class 'str_iterator'>

a = (2, 4)
b = a.__iter__()
print(type(b)) # виведе: <class 'tuple_iterator'>
print(b)  # виведе: <tuple_iterator object at ...>

# У об'єкта, що ітерується, немає методу __next__(), який використовується при ітерації
# Цей метод є у ітератора (механізму, який знає, як послідовно обробляти елементи об'єкта):
a = (2, 4)
## next(a) # TypeError: 'tuple' object is not an iterator
## a.__next__() # AttributeError: 'tuple' object has no attribute '__next__'
a = {10, 20}
print(next(a.__iter__())) # Виведе 10 або 20 — множина не гарантує порядок

# Ітератор має метод __next__(), який витягує з ітератора черговий елемент:
a = (2, 4)
b = a.__iter__()
print(b.__next__()) # виведе 2
print(b.__next__()) # виведе 4

# У ітераторів, як і у об'єктів, що ітеруються, є метод __iter__(). Однак у цьому випадку він повертає сам об'єкт-ітератор:
a = "hi"
b = a.__iter__()
c = b.__iter__()
print(c == b)  # True
print()


# Як перетворити клас на ітератор.
# !!! Для того щоб користувальницький клас міг виступати як ітератор необхідно, щоб у класі було визначено або успадковано такі методи:
# 1 - __iter__(self) - Метод, який вказує на те, що клас є ітератором (тобто підтримує ітераційний протокол). Метод має повернути ітератор
# 2 - __next__(self) - Викликається при кожній ітерації і повинен повернути чергове значення із послідовності. Якщо послідовність значень закінчена, генерується виняток StopIteration
# 3 - __getitem__(self, index) - Метод викликається лише у разі відсутності зазначених вище. У такому випадку Python сам створює ітератор на основі процедури вилучення індексу, починаючи з 0. Однак цей спосіб не рекомендований

# !!! Об'єкт, що ітерується - будь-який об'єкт, у якого реалізований метод __iter__, і який повертає ітератор для цього об'єкта
# !!! Саме цей метод і використовує функцію iter() для отримання ітератора
#
# !!! Ітератор - об'єкт, що володіє методом __next__. Цей метод повинен повертати таке доступне значення
# !!! Якщо доступних значень не залишилося, слід порушити виняток StopIteration. Також бажана наявність методу __iter__, який має повернути екземпляр ітератора

# Приклад створення класу, що ітерується, і ітератора
# Клас Товар (назва, ціна) для зберігання переліку товарів.
# Клас Кошик (список товарів, Ім'я користувача). Клас Кошик зробимо ітерованим для можливості проходу ним за допомогою циклу for:
class Goods:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Goods [name = {self.name}, price = {self.price}]"


class Basket:
    """ У цій реалізації не можна пройти по елементам Кошика в циклі """

    def __init__(self, user):
        self.user = user
        self.goods_list = list()

    def add_good(self, good):
        self.goods_list.append(good)

    def __str__(self):
        result = f"User: {self.user}\n"
        for good in self.goods_list:
            result += str(good) + "\n"
        return result

basket = Basket("Alexander_Ts")
a = Goods("Apple", 35)
b = Goods("Milk", 50)
basket.add_good(a)
basket.add_good(b)
# Побачимо, що в кошику є товар
print(basket)
# User: Alexander_Ts
# Goods [name = Apple, price = 35]
# Goods [name = Milk, price = 50]

# Спроба передати об'єкт кошика в цикл, спричинить помилку
# TypeError: 'Basket' object is not iterable
## for good in basket:
    ## print(good)

# Створимо клас Ітератор, який знатиме, як обробляти елементи кошика:
class BasketIterator:
    """ Клас ітератор, який знає як обробляти наповнення Кошика,
    щоб віддавати по одному елементу при кожному запиті
    """

    def __init__(self, goods_list):
        """При ініціалізації отримує список товарів
        і встановлює значення індексу 0"""
        self.goods_list = goods_list
        self.index = 0

    def __next__(self):
        """ Якщо значення індексу не виходить за межі розміру
        списку, надаємо елемент Кошика.
        В іншому випадку - викликаємо виняток"""
        if self.index < len(self.goods_list):
            res = self.goods_list[self.index]
            self.index = self.index + 1
            return res
        else:
            raise StopIteration

    def __iter__(self):
        return self

# І підключимо його до кошика

class Basket:
    def __init__(self, user):
        self.user = user
        self.goods_list = list()

    def add_good(self, good):
        self.goods_list.append(good)

    def __str__(self):
        result = f"User: {self.user}\n"
        for good in self.goods_list:
            result += str(good)+"\n"
        return result

    def __iter__(self):
        """Повертаємо екземпляр класу Ітератора"""
        return BasketIterator(self.goods_list)

basket = Basket("Alexander_Ts")
a = Goods("Apple", 35)
b = Goods("Milk", 50)
basket.add_good(a)
basket.add_good(b)
# Пройдемося циклом по елементах кошика
for good in basket:
    print(good)
# Додамо ще одну позицію товару до кошику
c = Goods("Oil", 100)
basket.add_good(c)

# І знову пройдемося циклом по елементах кошика
for good in basket:
    print(good)

# Імітація роботи циклу for через цикл while:
# for i in basket:
#     print(i)

itr = iter(basket)
# print(itr)
while True:
    try:
        good = next(itr)
        print(good)
    except StopIteration:
        break
