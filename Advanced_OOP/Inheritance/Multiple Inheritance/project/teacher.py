from project import Person
from project import Employee


class Teacher(Person, Employee):
    @staticmethod
    def teach():
        return "teaching..."