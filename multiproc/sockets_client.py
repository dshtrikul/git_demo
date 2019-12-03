from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from multiprocessing import Process, Lock
import random
import time
import sys
import pickle

port = 28463
host = 'localhost'


# messages = """multiprocessing is a package that supports spawning processes
# using an API similar to the threading module. The multiprocessing
# package offers both local and remote concurrency, effectively
# side-stepping the Global Interpreter Lock by using subprocesses
# instead of threads. Due to this, the multiprocessing module
# allows the programmer to fully leverage multiple processors
# on a given machine. It runs on both Unix and Windows\n"""

# messages = pickle.dumps(messages)   # comment out for 2nd option
# print(type(messages))

messages = """msg1
msg2
msg3"""


class Client(Process):
    def __init__(self):
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect((host, port))
            print(f'Connected to server on port {port}')
            Process.__init__(self)
        except ConnectionRefusedError:
            print(f'Server on port {port} is not started')
            sys.exit(1)

    def run(self):                                                   # multiline object
        for msg in messages.split('\n'):
            time.sleep(0.1*random.random())
            self.sock.send(f'PID {self.pid} | {msg}\n'.encode())   # length of msg ???? talk to aleksey
            print(f'sent > {msg, self.pid}')
        self.sock.send('*EOM*'.encode())
        self.sock.close()
        # while True:
        #     print('waiting for quit command')
        #     data = self.sock.recv(1024).decode()
        #     if data == 'quit':
        #
        #         print(f'PID {self.pid} connection timed out')
        #         break


if __name__ == '__main__':
    for i in range(10):
        client = Client()
        client.start()
