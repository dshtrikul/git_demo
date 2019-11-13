from parser import Parser
from app import App
from handler import Printer, Logger


class Main:

    def __init__(self):
        """
        Program's central managing point
        """
        self.logger = Logger()
        self.printer = Printer()
        self.parser = Parser()
        self.app = App()

    def get_args(self):                         # Calling to Parser
        """
        Wrapper function to simplify argument enclosure
        :rtype dict
        """
        return self.parser.get_arg_dict()

    def get_command_line_data(self):          # Calling to App
        """
        Wrapper function to retrieve list of handled commands

        :rtype list
        """
        self.app.construct_arg_dict(self.get_args())
        data = self.app.get_data_from_loop()
        return data

    def print(self):                          # Calling to Printer
        """
        Calling to handle printing
        :return: Nothing
        """
        self.printer.output(self.get_command_line_data())

    def log(self):                            # Calling to Logger
        """
        Calling to manage log saving
        :return: Nothing
        """
        self.logger.save(self.get_command_line_data())


if __name__ == '__main__':
    main = Main()
    main.log()

