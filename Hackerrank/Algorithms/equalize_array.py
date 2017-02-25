from itertools import groupby as g

n = int(input())

numbers = list(map(int,input().split()))

# https://stackoverflow.com/questions/1518522/python-most-common-element-in-a-list
#def most_common(L):
#    return max(g(sorted(L)), key=lambda(x, v):(len(list(v)),-L.index(x)))[0]
def most_common(lst):
    return max(set(lst),key=lst.count)

mode = most_common(numbers)
count = 0
for num in numbers:
    if num!=mode:
        count+=1
print(count)

