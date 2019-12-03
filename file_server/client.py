from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from multiprocessing import Process, Lock
from pathlib import Path
import sys
import time

port = 28475
host = 'localhost'


def init():
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))
        print(f'Connected to server on port {port}')
        return sock

    except ConnectionRefusedError:
        print(f'Server on port {port} is not started')
        sys.exit(1)


def run(filename, sock):
    Path('downloads/').mkdir(parents=True, exist_ok=True)

    try:
        sock.send(f'{filename}'.encode())
        print(f'requested {filename}')
        reply = sock.recv(1024).decode()
        print(reply)
        if reply == "<class 'FileNotFoundError'>":
            raise FileNotFoundError
        sock.send(f'ready'.encode())

    except FileNotFoundError:
        print(f'Error: {filename} not found on server')
        sock.close()
        sys.exit(1)

    sock.settimeout(3)
    path = Path(f'downloads/{filename}')
    new_path = path.with_name(path.stem + f'_{time.ctime()}' + path.suffix)

    while True:
        data = sock.recv(1024)
        if not data:
            break
        open(new_path, 'ab').write(data)
    sock.close()
    print(f'Got {filename}')


if __name__ == '__main__':
    Process(target=run, args=('UML Classroom.pdf', init())).start()
