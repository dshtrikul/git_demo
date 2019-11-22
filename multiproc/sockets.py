from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import pickle
from random import randint

port = randint(28559, 30000)
host = 'localhost'


def server():
    while True:
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.bind(('', port))
            sock.listen(5)
            print(f'Server started on port {port}')

            while True:
                conn, addr = sock.accept()
                data = conn.recv(1024).decode()
                conn.send(f'Hello to client {data}'.encode())
        except Exception as e:
            if isinstance(e, PermissionError):
                print(f'Port {port} is busy')
                continue


def client(num):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))

    # data = pickle.dumps(num)
    # sock.send(data)

    sock.send(f'{num}'.encode())
    print(f'client #{num} received >>> {sock.recv(1024).decode()}')
    sock.close()


def start_server():
    server_thr = Thread(target=server)
    server_thr.daemon = True
    server_thr.start()


def start_clients(num):
    for i in range(num):
        Thread(target=client, args=(i,)).start()


if __name__ == '__main__':
    start_server()
    start_clients(3)




