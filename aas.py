#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# rsimai@suse.com

import string

with open('/usr/share/dict/american') as fd:
    a =fd.read().splitlines()

letter = ['']
count = 0
word = ''

print "Words", len(a)

for i in range(0,26):
    x = string.ascii_lowercase[i]
    print "now for", x
    while True:
        word = a[count]
        if str.lower(word[:1]) == x:
            letter.append(word)
            count += 1
        else:
            print "Letter", x, "close at", count
            break
            
    
