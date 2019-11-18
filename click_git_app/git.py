import click
import subprocess as sp
import datetime
from pathlib import Path
lsep = "-" * 50


def save_to_log(output, command, lsep):
    filename = "log_file_" + f"{datetime.datetime.now():%Y-%d-%m--%H-%M-%S}.txt"
    output = filename + '\n' + lsep + '\n' + command + '\n' * 2 + output + lsep

    Path('logs/').mkdir(parents=True, exist_ok=True)
    with open(Path(f"logs/{filename}"), "w") as file:
        file.write(output)
    return f"{filename} saved"


@click.group()
def main():
    """More than GIT"""
    pass


@main.group()
def git():
    """
    Version control utility
    """
    pass

# python git.py git cmd status
# python git.py git cmd -log -- --help
@git.command(help='Pipe any command to git')
@click.argument('command')
@click.option('-log', 'log', is_flag=True)
def cmd(command, log):
    # print(command)
    # os.system('git status')                                  # Just execute code
    # subprocess.call(command, shell=True)
    command = 'git '+command
    p = sp.Popen(command, stdout=sp.PIPE, shell=True)
    # output = p.communicate()[0].decode()                     # via communicate()
    # rcode = p.returncode
    output = p.stdout.read().decode()                          # via stdout.read()

    if not log:
        print(output, f'\nexit code:{p.wait()}')

    if log:
        result = save_to_log(output, command, lsep)
        print(result)


if __name__ == "__main__":
    main()