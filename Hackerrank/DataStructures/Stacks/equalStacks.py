#def getHeights(stack):
#    return [sum(stack[i]) for i in range(3)]

#def sameValues(x):
#    return (x.count(x[0]) == len(x))

n1, n2, n3 = map(int,input().split())
stack =  [list(map(int,input().split()))[::-1] for _ in range(3)]

#heights = getHeights(stack)
heights = list(map(sum,stack))
tallestStackIndex = heights.index(max(heights)) #index of the tallest stack.
#while (not sameValues(heights)):
while len(set(heights)) > 1: # Sets has unique appearances of each number, this if its length is bigger than one there are more than 1 unique numbers in the list heights.
    element = stack[tallestStackIndex].pop() # Pop from the stack with the tallest size
    #heights = getHeights(stack) <- BAD
    heights[tallestStackIndex]-= element
    tallestStackIndex = heights.index(max(heights)) #index of the tallest stack.

print(heights[0])

