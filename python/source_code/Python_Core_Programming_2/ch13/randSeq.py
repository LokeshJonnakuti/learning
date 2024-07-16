#!/usr/bin/env python

import secrets

class RandSeq(object):
    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        return self

    def next(self):
        return secrets.choice(self.data)
