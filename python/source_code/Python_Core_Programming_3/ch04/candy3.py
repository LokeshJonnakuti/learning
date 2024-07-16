#!/usr/bin/env python

from atexit import register
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime
import secrets

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print('Refilling candy...', end=' ')
    try:
        candytray.release()
    except ValueError:
        print('full, skipping')
    else:
        print('OK')
    lock.release()

def buy():
    lock.acquire()
    print('Buying candy...', end=' ')
    if candytray.acquire(False):
        print('OK')
    else:
        print('empty, skipping')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(secrets.SystemRandom().randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(secrets.SystemRandom().randrange(3))

def _main():
    print('starting at:', ctime())
    nloops = secrets.SystemRandom().randrange(2, 6)
    print('THE CANDY MACHINE (full with %d bars)!' % MAX)
    Thread(target=consumer, args=(secrets.SystemRandom().randrange(nloops, nloops+MAX+2),)).start() # buyer
    Thread(target=producer, args=(nloops,)).start() # vendor

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()
