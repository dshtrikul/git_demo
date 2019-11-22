import os
def child():
    print('Hello from child', os.getpid())
    os._exit(0) # else goes back to parent loop
def parent():
    while True:
        newpid = os.fork()

        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)

        if input() == 'q': break


parent()

# ------------------------------------------------------
# import sys, os, time


# def counter(count):  # run in new process
#     for i in range(count):
#         time.sleep(0.5) # simulate real work
#         print('[%s] => %s' % (os.getpid(), i))
#
#
# for i in range(3):
#     pid = os.fork()
#     if pid != 0:
#         time.sleep(3)
#         print('Process %d spawned' % pid)  # in parent: continue
#     else:
#         counter(3) # else in child/new process
#         os._exit(0) # run function and exit
#
# print('Main process exiting.')             # parent need not wait

# ------------------------------------------------------
# parm = 0
# while True:
#     parm += 1
#     pid = os.fork()
#     if pid == 0: # copy process
#         os.execlp('python', 'python', str(parm)) # overlay program
#         assert False, 'error starting program' # shouldn't return
#     else:
#         print('Child is', pid)
#         if input() == 'q': break