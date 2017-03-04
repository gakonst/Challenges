n = int(input()) # Number of queries
def maxofTwo(val,test):
    if test > val:
        return test
    else:
        return val

stack = []
maxNum = 0
for _ in range(n):
    query = list(map(int,input().split(" ")))
    if query[0] == 1:
        stack.append(query[1])
        maxNum = maxofTwo(maxNum, query[1])
    elif query[0] == 2:
        stack.pop()
        if len(stack) == 0:
            maxNum = 0
        else:
            maxNum = max(stack) # Only search the whole stack for the max when popping
    else:
        print(maxNum)

