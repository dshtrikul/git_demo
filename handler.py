import datetime
from pathlib import Path


class Printer:

    def output(self, data):
        print('========  GIT DEMO ========')
        print(f"{datetime.datetime.now():%A, %d. %B %Y %H:%M}", '\n')
        print(data)


class Logger:

    def log_to_file(self, data):
        filename = "log_file_" + f"{datetime.datetime.now():%Y-%d-%m--%H-%M-%S}.txt"
        Path('logs/').mkdir(parents=True, exist_ok=True)
        with open(Path(f"logs/{filename}"), "w") as file:
            file.write(data)
            print(f"{filename} saved")


if __name__ == '__main__':

    p = Printer()
    # p.output(111)
    pp = Logger()
    pp.log_to_file("hello")
