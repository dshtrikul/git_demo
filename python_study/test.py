class Test:
    def __init__(self, name, age, newarg):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age}'
