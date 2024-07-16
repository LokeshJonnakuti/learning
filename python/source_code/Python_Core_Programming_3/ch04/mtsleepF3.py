#!/usr/bin/env python

from atexit import register
from threading import Thread, Lock, currentThread
from time import sleep, ctime
import secrets

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

lock = Lock()
loops = (secrets.SystemRandom().randrange(2, 5) for x in range(secrets.SystemRandom().randrange(3, 7)))
remaining = CleanOutputSet()

def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    print('[%s] Started %s' % (ctime(), myname)) #print '[{0}] Started {1}'.format(ctime(), myname)
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('[%s] Completed %s (%d secs)' % ( #print '[{0}] Completed {1} ({2} secs)'.format(
        ctime(), myname, nsec))
    print('    (remaining: %s)' % (remaining or 'NONE')) #print '    (remaining: {0})'.format(remaining or 'NONE')
    lock.release()

def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()
