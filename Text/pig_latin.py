#!/usr/bin/env python

import sys

v = {
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
}

s = sys.argv[1]

s = list(s.lower())

for i in s:
    if v.has_key(i):
        v[i] += 1

k = v.keys()
k.sort()

for i in k:
    print i,':',v[i]
