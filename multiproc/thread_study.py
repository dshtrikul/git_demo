"spawn threads until you type 'q'"
import _thread
import threading
import time
from random import random

# -----------------------------------------------
# def child(tid):
#     print('Hello from thread', tid)
#
#
# def parent():
#     i = 0
#     while True:
#         i += 1
#         _thread.start_new_thread(child, (i,))
#         if input() == 'q': break
#
# # parent()
# -----------------------------------------------
# def child_th(n):
#     count = 0
#     sum = 0
#     name = threading.current_thread().name
#     while count < n:
#         count += 1
#         tm = 1*random()
#         time.sleep(tm)
#
#         print(f'{name} >> {tm:.2f}')
#         sum += tm
#     print(f'{name} is finished at {sum:.2f}')
#
#
#
# # def parent_th(i=0):
# #     while True:
# #         inp = input('>')
# #         if inp == '':
# #             i += 1
# #             thr = threading.Thread(target=child_th, args=(i,))
# #             thr.start()
# #
# #         elif inp == 'q':
# #             break
# #         elif inp == 's':
# #             print(f'threading.active_count() >> {threading.active_count()}')
#
#
#
# def parent_th2(i=0, thr_n=2, sec=5):
#     while i <= thr_n:
#         i += 1
#         thr = threading.Thread(target=child_th, args=(sec,), name=f'Thread #{i}')
#         thr.start()
#         #
#         # elif inp == 'q':
#         #     break
#         # elif inp == 's':
#         print(f'threading.active_count() >> {threading.active_count()}')
#     print('Done')
#
# # parent_th()
# parent_th2()
# -----------------------------------------------
# with locks

#
# # lock = threading.Lock()
#
# def child_th_lc(n):
#     count = 0
#     sum = 0
#     name = threading.current_thread().name
#     while count < n:
#         count += 1
#         tm = 1
#         time.sleep(tm)
#         # lock.acquire()
#         with lock:
#             print(f'{name} >> {tm:.2f}')
#         # lock.release()
#         sum += tm
#     print(f'{name} is finished at {sum:.2f}')
#
#
# def parent_th2_lc(i=0, thr_n=2, sec=5):
#     while i <= thr_n:
#         i += 1
#         thr = threading.Thread(target=child_th_lc, args=(sec,), name=f'Thread #{i}')
#         thr.start()
#         print(f'threading.active_count() >> {threading.active_count()}')
#
#
# parent_th2_lc()
# -----------------------------------------------
# with locks via class


class CounterThread(threading.Thread):

    def __init__(self, sec=5):
        """
        Runs a new thread to count up to {sec} seconds
        :param sec: int
        """
        self.sec = sec
        self.lock = threading.Lock()
        threading.Thread.__init__(self)

    def run(self, count=0, sum=0):
        """Sleeps and prints its sleep time, counts up the total working time"""
        while count < self.sec:
            count += 1
            tm = 1*random()
            time.sleep(tm)
            with self.lock:
                open('log2.txt', "a").write(f'{self.name} >> {tm:.2f}\n')
            sum += tm
        print(f'{self.name} is finished at {sum:.2f}')


class Main:
    def __init__(self, thread_class, number, *args, **kwargs):
        """Wrapper to create a {number} of {thread_class} instances
        :param thread_class: cls
        :param number : int
        """
        tds = []
        for num in range(number):
            new_thread = thread_class(*args, **kwargs)
            new_thread.daemon = True                            # detach from main thread
            new_thread.start()
            tds.append(new_thread)
            print(f"{new_thread.name} created")
        for t in tds:                                           # await for all threads to close
            t.join()                                            # otherwise threads will close



main = Main(CounterThread, 3, 5)



