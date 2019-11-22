import os, time, sys

fifoname = '/tmp/pipefifo'  # must open same name


def sender(inp):
    pipeout = open(fifoname, 'wb', buffering=0) # open fifo pipe file as fd
    zzz = 0.5
    while True:
        time.sleep(zzz)
        msg = f'{inp} sleeped for {zzz} secs\n'.encode() # binary as opened here
        pipeout.write(msg)


if __name__ == '__main__':
    print(sys.argv)
    if not os.path.exists(fifoname):
        os.mkfifo(fifoname)  # create a named pipe file
    if len(sys.argv) > 1:
        # sender(sys.argv[-1]) # run as parent if no args
        sender(sys.argv[-1])  # run as parent if no args
    else:
        assert False
