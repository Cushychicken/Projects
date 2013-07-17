#!/usr/bin/env python

import sys
import re

if re.search('.*\.txt', sys.argv[1]):
    f = open(sys.argv[1])
    content = f.read()
    f = content.split()
    print 'Wordcount:', len(f)
else:
    f = sys.argv[1].split()
    print 'Wordcount:', len(f) 
