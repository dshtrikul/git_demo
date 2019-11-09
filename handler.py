import datetime
from pathlib import Path


class BaseHandler:

    def handle(self, data):
        for item in data:
            if item is not None:
                return item


class Printer(BaseHandler):

    def output(self, data):
        print('========  GIT DEMO ========')
        print(f"{datetime.datetime.now():%A, %d. %B %Y %H:%M}", '\n')
        print(self.handle(data))


class Logger(BaseHandler):

    def log_to_file(self, data):
        filename = "log_file_" + f"{datetime.datetime.now():%Y-%d-%m--%H-%M-%S}.txt"
        Path('logs/').mkdir(parents=True, exist_ok=True)
        with open(Path(f"logs/{filename}"), "w") as file:
            file.write(self.handle(data))
            print(f"{filename} saved")


if __name__ == '__main__':
    p = Printer()
    pp = Logger()
    pp.log_to_file("hello")
