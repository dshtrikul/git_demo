from socket import timeout as tx
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from multiprocessing import Process, Lock
import threading
import random
import time
import pickle

port = 28463
host = ''


class Sock:
    def __init__(self, port, host):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(5)
        print(f'Socket created on port {port}')

    def get_socket(self):
        return self.sock


class ClientHandler:
    def __init__(self, conn, address):
        self.connection = conn
        self.address = address

    def handle(self):
        while True:
            time.sleep(0.5*random.random())  # simulate work
            # try:
            data = self.connection.recv(1024).decode().splitlines()
            for item in data:
                if item == '*EOM*':
                    print(f'Reached EOM for {self.address} on {threading.currentThread().name}, total {threading.active_count()-1}')
                    conn_manager.thr_limiter.release()
                    # self.connection.close()
                    return
                print(f'>>> {item}')

            # if not data:


            # except tx:
            #     self.connection.send('quit'.encode())
            #     print('Connection closed')
            #     break


class ConnectionManager:
    def __init__(self, socket_obj):
        self.sock = socket_obj
        self.max_threads = 20
        self.thr_limiter = threading.BoundedSemaphore(self.max_threads)

    def run(self):
        while True:

            # print(f'{threading.enumerate()}')
            self.thr_limiter.acquire()
            conn, address = self.sock.accept()
            # conn.settimeout(3)
            client_handler = ClientHandler(conn, address)
            thread = threading.Thread(target=client_handler.handle)
            thread.start()
            print(f'Got new connection from {address}, {thread.name} started')




#
# class Server(Process):
#     def __init__(self):
#
#         try:
#             self.sock = socket(AF_INET, SOCK_STREAM)
#             self.sock.bind(('', port))
#             self.sock.listen(5)
#             # self.sock.settimeout(10)
#             # self.lock = Lock()
#             print(f'Server started on port {port}')
#             Process.__init__(self)
#
#         except Exception as e:
#             if isinstance(e, PermissionError):
#                 print(f'Port {port} is busy')
#
#
# class Counter(Server):
#
#     def __init__(self):
#         Server.__init__(self)
#
#
#     def run(self):
#         while True:
#             conn, addr = self.sock.accept()
#             conn.settimeout(1)
#             print(f'Got new connection from {addr}')
#             # import pdb; pdb.set_trace()
#             while True:
#                 time.sleep(0.5)  # to see that messages are not lost, but queued
#                 try:
#                     data = conn.recv(1024).decode().splitlines()
#
#                     for item in data:
#                         print(f'>>> {item}')
#                 except tx:
#                     conn.send('quit'.encode())
#                     print('Connection closed')
#                     break


if __name__ == '__main__':
    # server_process = Counter()
    # server_process.start()

    sock = Sock(port, host)
    conn_manager = ConnectionManager(sock.get_socket())
    conn_manager.run()

