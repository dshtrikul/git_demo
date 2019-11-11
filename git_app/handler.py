import datetime
from pathlib import Path


class BaseHandler:
    """
    Base class for processing the program output
    """

    def handle(self, data):
        """
        Iterates over input data list to discard the items with None value

        :param data: input data with items to be handled
        :type data: list
        :return: items other than none
        """
        for item in data:
            if item is not None:
                return item


class Printer(BaseHandler):
    """
    Specialization class to output data to STDOUT
    Extends 'BaseHandler' class
    """

    def output(self, data):
        """
        Generates and outputs the header for user's convenience to STDOUT
        Outputs received data to STDOUT

        :param data: Input data for processing
        :type data: String
        :return: None
        """
        print('========  GIT DEMO ========')
        print(f"{datetime.datetime.now():%A, %d. %B %Y %H:%M}", '\n')
        print(self.handle(data))


class Logger(BaseHandler):
    """
    Specialization class to log output data to a file
    Extends 'BaseHandler' class
    """

    def log_to_file(self, data):
        """
        Generates filename for sorting purposes and saves logfile to a dedicated directory

        :param data: Input data for processing
        :type data: String
        :return: None
        """

        filename = "log_file_" + f"{datetime.datetime.now():%Y-%d-%m--%H-%M-%S}.txt"
        Path('logs/').mkdir(parents=True, exist_ok=True)
        with open(Path(f"logs/{filename}"), "w") as file:
            file.write(self.handle(data))
            print(f"{filename} saved")


if __name__ == '__main__':
    p = Printer()
    pp = Logger()
    pp.log_to_file("hello")
