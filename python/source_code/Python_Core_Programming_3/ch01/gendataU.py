#!/usr/bin/env python

from distutils.log import warn as printf
from string import ascii_lowercase as lc
from time import ctime
import secrets

tlds = ( 'com', 'edu', 'net', 'org', 'gov' )

if hasattr(__builtins__, 'xrange'):
    myrng = xrange
else:
    myrng = range

for i in myrng(secrets.SystemRandom().randrange(5, 11)):
    dtint = secrets.SystemRandom().randrange(2**32)    # pick date
    dtstr = ctime(dtint)        # date string
    llen = secrets.SystemRandom().randrange(4, 7)      # login is shorter
    login = ''.join(secrets.choice(lc) for j in myrng(llen))
    dlen = secrets.SystemRandom().randrange(llen, 13)  # domain is longer
    dom = ''.join(secrets.choice(lc) for j in myrng(dlen))
    printf('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
        dom, secrets.choice(tlds), dtint, llen, dlen))
