from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import threading

port = 28475
host = ''


class Sock:
    def __init__(self, port, host):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(5)
        print(f'Socket created on port {port}')

    def get_socket(self):
        return self.sock


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
            client_handler = ClientHandler(conn, address)
            thread = threading.Thread(target=client_handler.handle)
            thread.start()
            print(f'Got new connection from {address}, {thread.name} started')


class ClientHandler:
    def __init__(self, conn, address):
        self.connection = conn
        self.address = address

    def send_data(self, file):
        while True:
            bytes = file.read(1024)
            if not bytes:
                break
            sent = self.connection.send(bytes)
            assert sent == len(bytes)
        print(f'Done')

    def handle(self):
        while True:
            filename = self.connection.recv(1024).decode()
            if filename:
                print(f'got request: {filename}')
                try:
                    file = open(filename, "rb")
                    self.connection.send(f'Server is starting transfer'.encode())
                    if self.connection.recv(1024).decode() == 'ready':
                        self.send_data(file)
                        break

                except FileNotFoundError as e:
                    print(f'No such file {filename}')
                    self.connection.send(f'{type(e)}'.encode())

        self.connection.close()


if __name__ == '__main__':
    sock = Sock(port, host)
    conn_manager = ConnectionManager(sock.get_socket())
    conn_manager.run()


