from student import Student
from exceptions import GroupLimitError

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set() # множина студентів

    def add_student(self, student):
        if len(self.group) >= 10:  # з len - це буде кількість студентів у групі
            raise GroupLimitError("В групі більше, ніж 10 студентів")
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + "\n"  # str(student) викликає метод __str__, і повертає рядок з інформацією про студента
        return f'Number:{self.number}\n{all_students}'

    def __eq__(self, other):
        return isinstance(other, Student) and str(self) == str(other)  # порівнює два студентів по рядках, які повертає __str__

    def __hash__(self):
        return hash(str(self))