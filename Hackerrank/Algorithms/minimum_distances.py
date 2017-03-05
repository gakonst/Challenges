'''def removeDups(seq): # Returns the unique elements of a list. Not Order preserving. Faster than list(set(x))
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def indices(lst, element):
    # if element occurs n times, the returned result has n-1 differences. Bc it is indexes we only
    # need to compare the i and i-1 element
    result = []
    other_offset = -1
    while True:
        try:
            #print('Offset = {}'.format(offset))
            offset = lst.index(element, other_offset+1)
            other_offset = lst.index(element,offset+1)
        except ValueError:
            return result
        result.append(offset-other_offset)'''

n = int(input())
array = list(map(int,input().split()))
minDistance = n
found = False
O(n^2)  Approach:
for i in range(n):
    for j in range(i+1,n):
        if array[i]==array[j]:
            found = True
            dist = abs(i-j)
            if (dist < minDistance):
                minDistance = dist

if found:
    print(minDistance)
else:
    print(-1)


'''Boss approach:
    #!/bin/python3

import sys

# Input array size
n = int(input().strip())

# Input array
A = [int(A_temp) for A_temp in input().strip().split(' ')]

# Create empty dictionary to keep track of element value and its last know position in the array
d={}

# Initialize minimum difference variable as one more than the maximum value(n-1) we can achieve
min_diff = n

# Going through each element in the array
for i in range(n):

# Try/Except statement to find record of the last known index for the element in the dictionary(for index difference calc), if unable to find the record then create the record
    try:

# min_diff equals minimum value between (the element index i and the last known location of the same element) and (min_diff)
        min_diff = min(i-d[A[i]],min_diff)

# Change the last known position of the element
        d[A[i]]=i

# Now if min_diff has value 1 then the code doesnt need to go further as its the minimum possible value for the answer
        if min_diff == 1:
            break

    except:
        d[A[i]]=i

# If min_diff is the same as initialized value meaning no element in input array is repeating then print -1 else the minimum difference value
if min_diff == n:
    print(-1)
else:
    print(min_diff)

    '''
