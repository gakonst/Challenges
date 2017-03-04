'''Keep in mind that; using multiple rotations, you can bring any number
into the quadrant that you desire. For any position in the upper left
quadrant (position [x][y], where x and y < n (and not 2*n)), you can
move numbers in any quadrant at the following positions to [x][y]:
[x][y] or // upper left quadrant [x][2*n-1-y] or // upper right quadrant
[2*n-1-x][y], or // lower left quadrant [2*n-1-x][2*n-1-y] // lower right quadrant
all you need to do then is, for every position (x and y) in the upper left quadrant,
you need to find the maximum of the four numbers at the above positions,
sum them and print the answer.
Note: Complexity is O(n) where n is the number of elements in the array'''
# If you just modify required output to print matrix after every flip it will be much harder.All you need here is to get the 4th element each time

q = int(input())
for _ in range(q):
    table = []
    maxSum = 0
    n = int(input())
    for i in range(2*n):
        table.append(list(map(int,input().split())))
    # Goal is to get the maximum sum of the upper-left submatrix tof the 2nx2n matrix
    # Allowed operations : reverse column or row.
    # a b b a
    # c d d c
    # c d d c
    # a b b a
    # Only same letters can be changed. Thus we want the max from each case.
    # This extends to bigger cases
    for i in range(n):
        for j in range(n):
            maxSum += max(table[i][j], \
                        table[i][2*n-j-1], \
                        table[2*n-i-1][j], \
                        table[2*n-i-1][2*n-j-1])
    print (maxSum)


