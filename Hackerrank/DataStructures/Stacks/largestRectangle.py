def getSize(height, start, end):
    return height*(end-start)

n = int(input())
hist = list(map(int,input().split()))

positions = []
heights = []
# stack[-1] is always the top of the stack, like stack.peek()
# https://www.youtube.com/watch?v=VNbkzsnllsU
# https://www.youtube.com/watch?v=ZmnqCZp9bBs
# https://www.hackerrank.com/challenges/largest-rectangle/editorial
maxArea = 0
#for position, height in enumerate(hist):
for position in range(0,len(hist)):
    height = hist[position]
    if (len(heights)==0):
        positions.append(position)
        heights.append(height)
    elif (height > heights[-1]): # hacky way to avoid using extra variable
        positions.append(position)
        heights.append(height)
    elif height < heights[-1]:
        # Pop as long as the stack is not empty and the examined value is less than the current stack top
        while (len(heights) and height < heights[-1]):
            start = positions.pop()
            currHeight = heights.pop()
            size = getSize(currHeight, start, position)
           # print(size)
            if size > maxArea:
                maxArea = size
        if (not len(heights) or height > heights[-1]):
            heights.append(height)
            positions.append(start)
# Used to clean up the stack
while (len(heights)):
    start = positions.pop()
    currHeight = heights.pop()
    size = getSize(currHeight, start, n) # size from stack end compared to the value popped
    if size > maxArea:
        maxArea = size

print(maxArea)
