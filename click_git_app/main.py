# self.parser = argparse.ArgumentParser()
# self.parser.add_argument('-add', nargs="?", default=False, metavar='Filename', help='Add a file to staging area')
# self.parser.add_argument('-commit', nargs="?", default=False, metavar='Filename', help='Commit changes')
# self.parser.add_argument('-status', action='store_const', const=True, default=False, help='Output current repo status')
# self.parser.add_argument('-a', action='store_true', help='all flag for. Usage: -add -a')
# self.parser.add_argument('-m', action='store_true', help='message flag. Usage: -commit -m')
# self.parser.add_argument('-v', action='store_true', help='verbose flag. Usage: -status -v')

import click


@click.group()
def main():
    pass


@click.command()
@click.argument('string', nargs=-1)
@click.option('-a', '-all', 'all', is_flag=True)
@click.option('-caps/-nocaps', default=False)
def add(string, all, caps):
    if all:
        print('do add -aa')
    elif string is not None and len(string) > 0
        if caps:
            print('caps!!!')
            string = string[0].upper()
        print(f'do add {string[0]}')
    else:
        print('exit')





main.add_command(add)



if __name__ == "__main__":
    main()
#
# @click.argument('command', type=click.Choice(['output', 'add', 'commit', 'status']))
# @click.option('-string') #, prompt='Message') # , nargs=-1
# @click.option('-r', '--repeat', 'repeat', type=click.Choice([repr(x) for x in [1, 2, 3]]))
# @click.option('-caps/-nocaps', default=False)
# @click.option('-a', '-all', 'all', is_flag=True)
# @click.option('-m', '--message')
# @click.option('-v', '--verbose', is_flag=True)
# def run(command, string, repeat, caps, all, message, verbose):
#     if command == 'output':
#         if caps:
#             print('caps!!!')
#             string = string.upper()
#
#         if repeat:
#             print((string+'\n')*eval(repeat))
#         else:
#             print(string)
#
#     if command == 'add':
#         print(type(all))
#         if all:
#             print('do add -aa')
#         if string is not None:
#             print(f'do add {string}')
#         else:
#             print('exit')
#
