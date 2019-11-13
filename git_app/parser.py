import argparse
import sys


class Parser:
    """
    Aggregates argument parsing functions
    """
    def __init__(self):

        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-add', nargs="?", default=False, metavar='Filename', help='Add a file to staging area')
        self.parser.add_argument('-commit', nargs="?", default=False, metavar='Filename', help='Commit changes')
        self.parser.add_argument('-status', action='store_const', const=True, default=False, help='Output current repo status')
        self.parser.add_argument('-a', action='store_true', help='all flag for. Usage: -add -a')
        self.parser.add_argument('-m', action='store_true', help='message flag. Usage: -commit -m')
        self.parser.add_argument('-v', action='store_true', help='verbose flag. Usage: -status -v')

    def get_arg_dict(self, foo=None):
        """
        Aggregate parsed arguments for further processing
        :param foo: some item
        :type foo: dict

        :rtype: dict
        :return: dict of argument - value pairs
        """

        arg_set = self.parser.parse_args()
        # import pdb; pdb.set_trace()
        return {
            'add': arg_set.add,
            'commit': arg_set.commit,
            'status': arg_set.status,
            'a': arg_set.a,
            'm': arg_set.m,
            'v': arg_set.v
        }

    def terminate(self):
        """
        Provide ability to terminate processing

        :raises: RuntimeError
        :returns: RuntimeError

        """
        print('Error: not enough arguments')
        self.parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    parser = Parser()
    print(parser.get_arg_dict())
