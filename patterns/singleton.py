class Employee:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'inst'):
            print(f'first creation of {cls}')
            cls.inst = super(Employee, cls).__new__(cls)
        return cls.inst


e = Employee()
m = Employee()
print(e, m)


class MetaSinlgeton(type):
    _inst = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            cls._inst[cls] = super(MetaSinlgeton, cls).__call__(*args, **kwargs)
        print(cls._inst)  # {class:obj}
        return cls._inst[cls]


class Log(metaclass=MetaSinlgeton):
    pass

class MyClass:
    pass


singleton2 = Log()
del Log

import singleton

logg = Log()
import pdb; pdb.set_trace()

logg2 = Log()
print(logg, logg2)

