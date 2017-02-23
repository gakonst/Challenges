n = int(input())
unsorted = []
for i in range(n):
    unsorted.append(int(input()))

output = sorted(unsorted)
for i in range(n):
    print (output[i])
