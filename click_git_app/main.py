import click, sys, subprocess

@click.group()
def main():
    """Click is a cool CLI utility"""
    pass


@click.command()
@click.argument('filename', nargs=-1)
@click.option('-a', '-all', 'all', is_flag=True)
@click.option('-caps/-nocaps', default=False)
@click.pass_context
def add(ctx, filename, all, caps):
    """Mimic the git add command"""
    if all:
        print('do add -aa')
    elif filename is not None and len(filename) > 0:
        if caps:
            print('caps!!!')
            filename = filename[0].upper()
        print(f'do add {filename[0]}')
    else:
        print(add.get_help(ctx))


@click.command()
@click.argument('commit_message', nargs=-1)
@click.option('-m', '-message', 'message', required=True)
@click.option('--show-hash', 'show_hash', flag_value=True)
@click.pass_context
def commit(ctx, commit_message, message, show_hash):
    "Mimic the git commit command"
    if message:
        print(f'do commit {message}')
        if show_hash:
            print('HASH '+str(hash(message)))

    else:
        print(commit.get_help(ctx))


@click.command()
@click.argument('some_words', required=True)
@click.option('-v', '--verbose', 'verbose', count=True, help="Choose from ['-v', '-vv', '-vvv']", required=True)
@click.pass_context
def talk(ctx, some_words, verbose):
    """Print words some number of times"""
    if verbose == 0:
        print(talk.get_help(ctx))
        sys.exit()
    if some_words:
        click.confirm('Proceed?', abort=True)
        print(f'versosity level is {verbose}')
        print((some_words+' ')*verbose)


@click.command()
@click.option('-f', '--file', 'open_file', required=True, type=click.File('r'))
@click.option('-exec/-noexec', 'exec', default=False)
@click.option('-s', '--save', 'save_to_file', type=click.File('a'))
def execute(open_file, save_to_file, exec):
    """Execute script in shell, write output to file"""
    if open_file:
        commands = open_file.read()
        print(commands)
        if exec:
            for line in commands.split('\n'):
                output = subprocess.check_output(line, shell=True).decode('cp1251')
                print(output)
                if save_to_file:
                    save_to_file.write(output)


@click.command()
@click.option('-s', '--seconds', 'seconds', required=True, type=click.Choice([repr(x) for x in range(100, 110)]))
def count(seconds):
    """Show a progress bar feature"""
    import time, random
    with click.progressbar(range(int(seconds)), label='PROGRESS') as bar:
        for item in bar:
            time.sleep(random.randint(5, 400)*0.0005)


main.add_command(add)
main.add_command(commit)
main.add_command(talk)
main.add_command(execute)
main.add_command(count)


if __name__ == "__main__":
    main()
