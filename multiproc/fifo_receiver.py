import os, time, sys

fifoname = '/tmp/pipefifo'  # must open same name


def receiver():
    pipein = open(fifoname, 'br', buffering=0) # open fifo as text file object
    while True:
        line = pipein.readline()[:-1] # blocks until data sent
        if line == b'':
            print('No conn')
            time.sleep(3)
        else:
            print(f'Parent {os.getpid()} got {line} at {time.time()}')


if __name__ == '__main__':
    print(sys.argv)
    if not os.path.exists(fifoname):
        os.mkfifo(fifoname) # create a named pipe file
    if len(sys.argv) == 1:
        receiver() # run as parent if no args
    else:  # else run as child process
        assert False