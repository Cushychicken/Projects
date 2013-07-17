#!/usr/bin/env python

import sys

s = sys.argv[1]
s = s.lower()
s = list(s)

if s == s[::-1]:
    print "It's a palindrome!"
else:
    print 'Not a palindrome.'
