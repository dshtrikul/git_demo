from parse import Parser
from app import App
from handler import Printer, Logger


if __name__ == '__main__':
    logger = Logger()
    printer = Printer()
    parser = Parser()
    app = App(parser.get_arg_dict())
    # print(parser.get_arg_dict())
    data = app.get_data_from_loop()

    printer.output(data)
    logger.log_to_file(data)
