import argparse


class Parser:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-add', nargs="?", default=False, metavar='{Filename}', help='Add a file to staging area')
        self.parser.add_argument('-commit', nargs="?", default=False, metavar='{Filename}', help='Commit changes')
        self.parser.add_argument('-status', action='store_const', const=True, default=False, help='Output current repo status')
        self.parser.add_argument('-a', action='store_true', help='all flag for. Usage: -add -a')
        self.parser.add_argument('-m', action='store_true', help='message flag. Usage: -commit -m')
        self.parser.add_argument('-v', action='store_true', help='verbose flag. Usage: -status -v')

    def get_arg_dict(self):
        p = self.parser.parse_args()
        return {
            'add': p.add,
            'commit': p.commit,
            'status': p.status,
            'a': p.a,
            'm': p.m,
            'v': p.v
        }


if __name__ == '__main__':
    parser = Parser()
    print(parser.get_arg_dict())
