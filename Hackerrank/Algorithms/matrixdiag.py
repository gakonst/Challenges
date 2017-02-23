#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
sum = 0
sumother=0
for i in range(0,n):
    sum+=a[i][i]
    sumother+=a[n-1-i][n-1-i]
diff = abs(sum-sumother)
print diff
    