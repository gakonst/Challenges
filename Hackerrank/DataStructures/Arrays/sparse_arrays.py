import collections

# https://docs.python.org/2/library/collections.html#collections.defaultdict
# https://stackoverflow.com/questions/19629682/ordereddict-vs-defaultdict-vs-dict
# Much better
#values = collections.defaultdict(int)
for _ in range(int(input())):
    print (values)
    values[input()] += 1
for _ in range(int(input())):
    print(values[input()])

'''Inneficient but does the job:
strings = []
    for _ in range(int(input())):
        strings.append(input())
    for _ in range(int(input())):
        print (strings.count(input()))
'''
