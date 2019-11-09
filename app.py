from parse import Parser
p = Parser()


class App:

    def __init__(self, arg_dict):
        self.add = arg_dict['add']
        self.commit = arg_dict['commit']
        self.status = arg_dict['status']
        self.a = arg_dict['a']
        self.m = arg_dict['m']
        self.v = arg_dict['v']

    def add_func(self):
        if self.add or self.add is None:
            if self.a:
                return 'do -add -a'                # Do something useful here
            if self.add:
                return f'do -add {self.add}'
            else:
                p.terminate()

    def commit_func(self):
        if self.commit or self.commit is None:
            if self.m:
                return 'do -commit -m'
            if self.commit:
                return f'do commit {self.commit}'
            else:
                p.terminate()

    def status_func(self):
        if self.status and self.v:
            return 'do -status -v'
        if self.status and not self.v:
            return 'do status'

    def get_data_from_loop(self):
        return [self.add_func(), self.commit_func(), self.status_func()]


if __name__ == '__main__':
    d = {'add': '99999', 'commit': True, 'status': False, 'a': False, 'm': False, 'v': False}
    app = App(d)
    app.get_data_from_loop()
