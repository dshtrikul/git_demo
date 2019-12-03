import shelve
from test import Test

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'},
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'},
# test = Test('dmytro', 29)

with shelve.open('people-shelve-test') as db:
    # db['bob'] = bob
    # db['sue'] = sue
    #
    #db['test'] = test
    # db_test = db['test']
    # print(type(db_test))
    # print(db_test)

    # sue2 = db['sue']
    import pdb; pdb.set_trace()    # fetch sue
    pass
    # sue2['pay'] = 999              # update record (item,)
    # print(sue2)                 # (item,) tuple
    # tom = db['tom']             # add a new record
    # print(list(db.items()))
