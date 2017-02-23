#!/bin/python3

def summation(x):
    return x*(x+1)>>1

n = int(input())
for i in range(n):
    number = int(input()) -1
    threes = number // 3 # numbers divisible with 3
    fives = number // 5 # 5
    fifteens = number//15 # 15, this is subbed so that we exclude all that are divisible by both

    total = 3*summation(threes)+5*summation(fives)-15*summation(fifteens)
    print (total)


