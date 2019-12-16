from abc import ABCMeta, abstractmethod


class Parts(metaclass=ABCMeta):
    def __str__(self):
        return self.__class__.__name__


class Chassis(Parts):
    pass


class Wings(Parts):
    pass


class Engine(Parts):
    pass


class Constructor(metaclass=ABCMeta):
    def __init__(self):
        self.parts = []
        self.assemble()

    def __str__(self):
        return self.__class__.__name__

    @abstractmethod
    def assemble(self):
        pass

    def get_parts(self):
        return [str(x) for x in self.parts]

    def add_part(self, part):
        self.parts.append(part)


class Car(Constructor):
    def assemble(self):
        self.add_part(Chassis())
        self.add_part(Engine())


class Plane(Constructor):
    def assemble(self):
        self.add_part(Chassis())
        self.add_part(Engine())
        self.add_part(Wings())


vehicle_type = input('Which vehicle? > ')
vehicle = eval(vehicle_type)()
print(f'{str(vehicle)} with parts: {", ".join(vehicle.get_parts())}')
