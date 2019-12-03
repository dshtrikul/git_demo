import pickle

# there is a possibility to make item-specific pickle files for optimization of large Databases
# search glob.glob

if __name__ == '__main__':

    filename = 'people-pickle_pickle'
    db = {
        'bob': {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'},
        'sue': {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'},
        'tom': {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None},
    }

    with open(filename, 'wb') as dbfile:  # wb = write&bytes
        pickle.dump(db, dbfile)

    with open(filename, 'rb') as dbfile:  # wb = write&bytes
        db_unpickled = pickle.load(dbfile)


    print(db_unpickled)
    # check return

    while len(db_unpickled) is not 1:
        db_unpickled.pop(list(db_unpickled.keys())[-1])
        # delete last key # keys() is not subscriptable, need to use list()
    with open(filename, 'wb') as dbfile:
        pickle.dump(db_unpickled, dbfile)
        print('changes saved')





