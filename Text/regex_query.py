#!/usr/bin/env python

import re
import sys

string = ''
regex = ''

if len(sys.argv) > 1:
    string = sys.argv[1]
    regex = sys.argv[2]
else:
    string = raw_input('Enter the string to test: ')
    regex = raw_input('Enter the regex to test :')

result = re.search(regex,string)
if result:
    print 'Text matches.'
    c = result.groups()
    if c:
        print 'Captures: ', result.groups()
else:
    print 'No match.'
