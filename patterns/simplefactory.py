# from abc import ABCMeta, abstractmethod
#
#
# class Person(metaclass=ABCMeta):
#     @abstractmethod
#     def __init__(self):
#         pass
#
#
# class HR(Person):
#     def __init__(self, name):
#         super().__init__()
#         print(f"HR {name} is created")
#
#
# class Engineer(Person):
#     def __init__(self, name):
#         super().__init__()
#         print(f"Engineer {name} is created")
#
#
# class PersonFactory:
#     @classmethod
#     def create_person(cls, designation, name):
#         return eval(designation)(name)
#
#
# if __name__ == "__main__":
#     designation = input("Please enter the designation - ")
#     name = input("Please enter the person's name - ")
#     inst = PersonFactory.create_person(designation, name)
#     print(inst)

# --------------------------

# from abc import ABCMeta, abstractmethod
#
#
# class Person(metaclass=ABCMeta):
#     @abstractmethod
#     def __init__(self):
#         pass


class HR:
    def __init__(self, name):
        super().__init__()
        print(f"HR {name} is created")


class Engineer:
    def __init__(self, name):
        super().__init__()
        print(f"Engineer {name} is created")


class PersonFactory:
    @classmethod
    def create_person(cls, designation, name):
        return eval(designation)(name)


if __name__ == "__main__":
    designation = input("Please enter the designation - ")
    name = input("Please enter the person's name - ")
    inst = PersonFactory.create_person(designation, name)
    print(inst)