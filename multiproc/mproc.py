import os
from multiprocessing import Process, Lock, Pipe
import time

#  ---------------------------------------------------------------------------------
# def whoami(label, lock):
#     with lock:
#         print(f"name {label}, pid {os.getpid()}, {__name__}")
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     whoami('function call', lock)
#
#     p = Process(target=whoami, args=('spawned child', lock))
#     p.start()
#     p.join()
#
#     for i in range(5):
#         Process(target=whoami, args=(f'run process {i}', lock)).start()
#         time.sleep(0.7)  # Main process exits last because of join()
#
#     with lock:
#      print('Main process exit.')


#  ---------------------------------------------------------------------------------
import inspect


# def send(pipe):
#     """
#     send object to parent on anonymous pipe
#     """
#     pipe.send(['Hello from send func'])
#     pipe.close()
#
#
# def send_and_reply(pipe):
#     """
#     send and receive objects on a pipe
#     """
#     pipe.send(dict(Hello='from send and reply'))
#     time.sleep(1)
#     reply = pipe.recv()
#     print('send_and_reply got reply:', reply)
#
#
# if __name__ == '__main__':
#     (parentEnd, childEnd) = Pipe()
#     send = Process(target=send, args=(childEnd,))
#     send.start()                                                # spawn child with pipe
#     print('parent got:', parentEnd.recv())                      # receive from child
#     parentEnd.close()                                           # or auto-closed on gc
#
#     (parentEnd, childEnd) = Pipe()
#     send_and_reply = Process(target=send_and_reply, args=(childEnd,))
#     send_and_reply.start()
#
#     print('parent got:', parentEnd.recv())                      # receive from child
#     parentEnd.send({'Hi from parent': True})                     # send to child
#     parentEnd.close()
#
#     send_and_reply.join()                                                # wait for child exit
#     print('parent exit')

#  -------------------------------------------------------------------------------
import time, queue, os, random
from multiprocessing import Process, Queue


class Counter(Process):
    def __init__(self, begin_num, queue):
        self.num = begin_num
        self.q = queue
        Process.__init__(self)

    def run(self):
        for i in range(5):
            time.sleep(0.9*random.random())
            self.num += 1
            self.q.put([self.pid, self.num, time.time()])
            print(f'>>> {self.pid} : {self.num}')


print(f'Starting with PID {os.getpid()}')

q = Queue()
c_1 = Counter(0, q)
c_100 = Counter(100, q)
c_1000 = Counter(1000, q)
for c in [c_1, c_100, c_1000]:
    c.start()

for i in range(20):
    time.sleep(0.8*random.random())
    try:
        data = q.get(timeout=3)
    except queue.Empty:
        print('No data...')
    else:
        print(f'fetched from queue {data[:2]}, posted {time.time() - data[-1]:.3f} sec. ago')

for c in [c_1, c_100, c_1000]:
    c.join()

print(f'finished, {os.getpid()} with exitcode {c_1000.exitcode}')
