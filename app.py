class App:

    def __init__(self, arg_dict):
        self.add = arg_dict['add']
        self.commit = arg_dict['commit']
        self.status = arg_dict['status']
        self.a = arg_dict['a']
        self.m = arg_dict['m']
        self.v = arg_dict['v']

    def add_func(self):
        if self.a:
            return 'do -add -a'                # Do something useful here
        if self.add is not None:
            return f'do -add {self.add}'

    def commit_func(self):
        if self.m:
            return 'do -commit -m'
        if self.commit is not None:
            return f'do commit {self.commit}'

    def status_func(self):
        if self.status and self.v:
            return 'do -status -v'
        if self.status and not self.v:
            return 'do status'

    def get_data_from_loop(self):
        if self.add or self.add is None:
            return self.add_func()

        if self.commit or self.commit is None:
            return self.commit_func()

        if self.status:
            return self.status_func()


if __name__ == '__main__':
    d = {'add': '99999', 'commit': True, 'status': False, 'a': False, 'm': False, 'v': False}
    app = App(d)
    app.get_data_from_loop()
