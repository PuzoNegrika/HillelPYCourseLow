from human import Human

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name) # super() - функція, яка дозволяє викликати методи батьківського класу з класу-нащадка
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} year old, {self.gender}, record book: {self.record_book}"