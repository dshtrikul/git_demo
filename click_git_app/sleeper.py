import sys
import time
import signal
import os


def construct_signals():
    signal.signal(signal.SIGHUP, receive_signal)
    signal.signal(signal.SIGINT, receive_signal)
    signal.signal(signal.SIGQUIT, receive_signal)
    signal.signal(signal.SIGILL, receive_signal)
    signal.signal(signal.SIGTRAP, receive_signal)
    signal.signal(signal.SIGABRT, receive_signal)
    signal.signal(signal.SIGBUS, receive_signal)
    signal.signal(signal.SIGFPE, receive_signal)
    # signal.signal(signal.SIGKILL, receive_signal)
    signal.signal(signal.SIGUSR1, receive_signal)
    signal.signal(signal.SIGSEGV, receive_signal)
    signal.signal(signal.SIGUSR2, receive_signal)
    signal.signal(signal.SIGPIPE, receive_signal)
    signal.signal(signal.SIGALRM, receive_signal)
    signal.signal(signal.SIGTERM, receive_signal)


def receive_signal(signum, frame):
    print(f"\n>>>>>>>>  Signal {signum} received <<<<<<<<<\n")
    if signum == 15:
        sys.exit()
    elif signum == 2:
        # os.system(f'kill -20 {signum}')
        i = input('Y/y to kill the process: ')
        if i in ['Y', 'y', 'yes']:
            sys.exit()
        else:
            print('Continuing...')


def show_init():
    print(sys.argv)
    print('Waiting')
    print(f'PID:{os.getpid()}')


def sleep(seconds):
    counter = 0
    while seconds > counter:
        print('.', end='')
        sys.stdout.flush()
        time.sleep(1)
        counter += 1

    sys.stdout.write('\nDone\n')
    sys.exit()


if __name__ == "__main__":
    construct_signals()
    show_init()
    sleep(int(sys.argv[1]))


