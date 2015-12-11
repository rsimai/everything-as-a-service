#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# rsimai@suse.com
# Hackweek 13, learning Python

from string import upper, lower, ascii_lowercase
from random import randint

with open('/usr/share/dict/american', 'r') as fd:
    a =fd.read().splitlines()            # get all words into this list

results = ['']                           # to store the usable (a-z) stuff from the dictionary
count = 0

print
print "Here's where the Cloud goes next year:"
print

for i in range(0,26):
    x = ascii_lowercase[i]               # need a-z
    mark1 = count                        # letter starts at that position
    while True:
        word = a[count]                  # read word to examine
        if lower(word[:1]) == x:         # see if the first letter still matches
            results.append(word)         # add to the results
            count += 1                   # count up
        else:
            mark2 = count - 1            # letter ends at that position
            rand = randint(mark1, mark2) # get some random number inbetween the marks
            first = upper(a[rand][:1])   # just formatting
            out = first + "aaS : " + first + a[rand][1:] + " as a Service"
            print out                    # print it
            break
            
print
