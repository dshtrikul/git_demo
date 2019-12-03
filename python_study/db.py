"""
Example case of sending dicts to a flat file using item separators and repr, eval
"""



dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def storeDbase(db, dbfilename=dbfilename):
    "formatted dump of database to flat file"
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
            # 'value' should be string to use STDOUT to file >> repr(value)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()


def loadDbase(dbfilename=dbfilename):
    "parse data to reconstruct database"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            # eval to turn strings python types
            field = input()
        db[key] = rec
        key = input()
    return db



if __name__ == '__main__':

    db = {
        'bob': {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'},
        'sue': {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'},
        'tom': {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None},
    }

    storeDbase(db)
    dd = loadDbase()
    print(dd.keys())
