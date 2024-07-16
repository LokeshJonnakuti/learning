#!/usr/bin/env python

from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime
import secrets

tlds = ( 'com', 'edu', 'net', 'org', 'gov' )

for i in range(secrets.SystemRandom().randrange(5, 11)):
    dtint = secrets.SystemRandom().randrange(maxsize)  # pick date
    dtstr = ctime(dtint)        # date string
    llen = secrets.SystemRandom().randrange(4, 7)      # login is shorter
    login = ''.join(secrets.choice(lc) for j in xrange(llen))
    dlen = secrets.SystemRandom().randrange(llen, 13)  # domain is longer
    dom = ''.join(secrets.choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
        dom, secrets.choice(tlds), dtint, llen, dlen))
