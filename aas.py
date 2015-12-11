#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# rsimai@suse.com

from string import upper, lower, ascii_lowercase
from random import randint

with open('/usr/share/dict/american') as fd:
    a =fd.read().splitlines()

letter = ['']
results = ['']
count = 0
word = ''

for i in range(0,26):
    x = ascii_lowercase[i]
    mark1 = count
    while True:
        word = a[count]
        if lower(word[:1]) == x:
            letter.append(word)
            count += 1
        else:
            mark2 = count - 1
            rand = randint(mark1, mark2)
            first = upper(a[rand][:1])
            out = first + "aaS : " + first + a[rand][1:] + " as a Service"
            print out
            break
            
    
