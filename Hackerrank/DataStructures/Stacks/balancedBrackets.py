n = int(input()) # number of cases

start = ['(','[','{']
end   = [')',']','}']

def indexes(lst,symbol):
    return [i for i,x in enumerate(lst) if x == symbol]

def isEmpty(stack):
    if len(stack) == 0 :
        return True
    else:
        return False

for _ in range(n):
    accepted = True
    brackets = input()
    stack = []
    for symbol in brackets:
        if accepted:
            if symbol in start:
                stack.append(symbol)
            else:
                if isEmpty(stack):
                    accepted = False
                    break

                # pop, if symbol indexes match okay, else false
                removed = stack.pop()
                indexStart = start.index(removed) # corresponding bracket in the start list
                indexEnd = end.index(symbol)
                if indexStart != indexEnd:
                    accepted = False

    if accepted and isEmpty(stack):
        print ('YES')
    else:
        print('NO')

''' Short version:

table =  { ')': '(', ']':'[', '}':'{' }
for _ in range(int(input())):
    stack = []
    for x in input():
        if stack and table.get(x) == stack[-1]:
            stack.pop()
        else:
            stack.append(x)
    print("NO" if stack else "YES")
'''
