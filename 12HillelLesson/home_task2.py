class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}, description: {self.description}, dimensions: {self.dimensions}"


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        result = f"User: {self.user}"
        result += f"\nItems:"
        for item, cnt in self.products.items():
            result += f"\n{item.name}: {cnt} pieces"
        return result

    def get_total(self):
        total = 0
        for item, cnt in self.products.items():
            total += item.price * cnt # беремо ціну одного товару (item.price), множимо на кількість (count), додаємо до змінної total
        return total


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""
assert cart.get_total() == 40


# ДЛЯ СЕБЕ
# навіщо нам метод __str__?
# __str__ — це метод, який каже Пайтону, як виглядає об’єкт, коли ми його друкуємо через print() (тобто типу print`a)
# Наприклад:
# print(lemon) # має вивести щось типу: lemon, price: 5

# for key in словник