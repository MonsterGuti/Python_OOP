from project import animal


class Tiger(Animal):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 45)
